#!/bin/sh

# write_po_files_for_directory() {
#     for lang in ${SUPPORTED_LANGUAGES}; do
#         DIR="locales/$lang/LC_MESSAGES/$1"
#         mkdir -p $DIR
#         xgettext \
#         --add-comments \
#         --check=bullet-unicode \
#         --check=ellipsis-unicode \
#         --check=quote-unicode \
#         --check=space-ellipsis \
#         --color \
#         --copyright-holder="TastyAndTheCats" \
#         --default-domain="$1" \
#         --extract-all \
#         --force-po \
#         --language=Python \
#         --no-wrap \
#         --sort-output \
#         --strict \
#         --width=120 \
#         --output-dir=$DIR \
#         --output="$2.po" \
#         --directory="$1/" \
#         $2.py
#         msgfmt -o $DIR/$2.mo $DIR/$2
#     done
# }

# creates a merged base.pot from all of the translatable strings in a given file
create_po_template(){
    xgettext --default-domain="base" --copyright-holder="TastyAndTheCats" -j --sort-by-file -o locales/base.pot $1/$2.py
}

# copies or merges base.pot into a language-specific base.po, which can be given to a translator (or chatGPT'd)
copy_or_merge_pot_to_po(){
    DIR="locales/$1/LC_MESSAGES"
    filename=$DIR/base.po
    echo $filename
    mkdir -p $DIR
    if [ -f "$filename" ]; then
        msgmerge --update $filename locales/base.pot
    else
        cp locales/base.pot $filename
    fi
}

# make sure locales exists and refresh base.pot to nothing
mkdir -p locales/
rm locales/base.pot
touch locales/base.pot

# absorb translation-marked strings and build base.pot
create_po_template src/chat prompts
# create_po_template src run
# create_po_template data/models __init__

# replace the charset= value, for wahtever reason the cli option doesn't seem to work and the tests fail if this isn't set
sed -i 's/charset=CHARSET/charset=UTF-8/g' locales/base.pot

# copy or merge the new .pot file into the language-specific .po files
for lang in ${SUPPORTED_LANGUAGES}; do
    copy_or_merge_pot_to_po $lang
done


