import os
import sys
import gettext


if os.getenv("TESTING"):
    lang = "en"
else:
    lang = sys.argv[1] if len(sys.argv) > 1 else "en"

print(lang)

gettext.bindtextdomain("base", "./locale")
gettext.textdomain("base")
translations = gettext.translation("base", localedir="locales", languages=[lang])
translations.install()

translate = translations.gettext
