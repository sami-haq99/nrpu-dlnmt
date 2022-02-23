#!/bin/bash
src=en
tgt=de
lang=en-de
prep=$OUTDIR
tmp=$prep/tmp
orig=orig
dev=dev/newstest2013

for entry in $(find . -name '*.sgm' -maxdepth 1 -type f -not -path '*/\.*' | sed 's/^\.\///g' | sort); do
    fname=${entry%-*}
    echo $fname
    echo $entry
    for l in $src $tgt; do
    if [ "$l" == "$src" ]; then
        t="src"
    else
        t="ref"
    fi
    grep '<seg id' $entry | \
        sed -e 's/<seg id="[0-9]*">\s*//g' | \
        sed -e 's/\s*<\/seg>\s*//g' | \
        sed -e "s/\’/\'/g" > ../en-de-text/$entry.txt
    echo "$l"
	done
done


echo "pre-processing test data..."