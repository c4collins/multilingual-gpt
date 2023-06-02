import os
import sys
import gettext

gettext.bindtextdomain("base", "./locale")
gettext.textdomain("base")
translations = gettext.translation(
    "base", localedir="locales", languages=[sys.argv[1] if len(sys.argv) > 1 else "en"]
)
translations.install()

translate = translations.gettext
