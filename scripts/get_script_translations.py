import fileinput
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_TOKEN")
languages = os.getenv("SUPPORTED_LANGUAGES").split(" ")


print("checking")

for lang in [l for l in languages if l != "en"]:
    path = os.path.join("locales", lang, "LC_MESSAGES")
    filepath = os.path.join(path, "base.po")

    msgid = None
    msgstr = None

    po_file_lines = []

    with open(filepath, "r") as po_file:
        for line in po_file.readlines():
            if line.startswith("msgid"):
                msgid = line.split(" ", 1)[1].strip().strip('"')
                if not msgid:
                    msgid = None
                po_file_lines.append(line)
            elif msgid and line.startswith("msgstr"):
                msgstr = line.split(" ", 1)[1].strip().strip('"')
                if not msgstr:
                    print(f"translating `{msgid}` to `{lang}`", end=" => ")
                    messages = [
                        {
                            "role": "system",
                            "content": f"Translate from `en` to `{lang}`: {msgid}",
                        }
                    ]
                    gpt_translation = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=messages,
                    )
                    translation_text = gpt_translation.choices[0].message.content
                    print(translation_text)
                    po_file_lines.append(f'msgstr "{translation_text}"')
                else:
                    po_file_lines.append(line)
            else:
                po_file_lines.append(line)

    with open(filepath, "w") as po_file:
        for line in po_file_lines:
            po_file.write(line)
