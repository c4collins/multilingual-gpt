import os
import sys
import gettext

lang = sys.argv[1] if len(sys.argv) > 1 else "en"

gettext.bindtextdomain("base", "./locale")
gettext.textdomain("base")
translations = gettext.translation("base", localedir="locales", languages=[lang])
translations.install()

translate = translations.gettext
