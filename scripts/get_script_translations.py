import os
from typing import List
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_TOKEN")
languages = os.getenv("SUPPORTED_LANGUAGES").split(" ")


def get_translation(messages):
    print(messages[0]["content"], end=" => ")
    gpt_translation = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    translation_text = gpt_translation.choices[0].message.content
    print(translation_text)
    return translation_text


def read_and_translate_file(filepath) -> List[str]:
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
                    messages = [
                        {
                            "role": "system",
                            "content": f"Translate from `en` to `{lang}`: {msgid}",
                        }
                    ]
                    translation_text = get_translation(messages)
                    po_file_lines.append(f'msgstr "{translation_text}"')
                    msgid = None
                else:
                    po_file_lines.append(line)
                    msgid = None
            else:
                po_file_lines.append(line)
                msgid = None
    return po_file_lines


def write_file(filepath, file_content):
    with open(filepath, "w") as file:
        for line in file_content:
            file.write(line)


def process_file_for_one_language(lang: str):
    path = os.path.join("locales", lang, "LC_MESSAGES")
    filepath = os.path.join(path, "base.po")
    po_file_lines = read_and_translate_file(filepath)
    write_file(filepath, po_file_lines)


if __name__ == "__main__":
    for lang in [l for l in languages if l != "en"]:
        process_file_for_one_language(lang)
