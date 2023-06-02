#!/bin/sh

# converts the base.po files into base.mo files for the machine to read
format_messages_for_machines(){
    DIR="locales/$1/LC_MESSAGES"
    msgfmt -o $DIR/base.mo $DIR/base
}

# convert the .po files to .mo files once they're translated
for lang in ${SUPPORTED_LANGUAGES}; do
    format_messages_for_machines $lang
done