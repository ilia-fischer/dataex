#! /bin/bash
rm -rf dat
mkdir dat
cd dat

for i in `ls ../*.json`; do
    echo $i
    url=`jq -r ".url" "$i"`
    echo $url
    wget $url -O `basename $i`
done
