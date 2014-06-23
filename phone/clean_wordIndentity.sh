#! /bin/bash

# filter out the lines with value 'DX' at the column 'Phone' ($16 in sm_train.data)
#cat sm_train.data | awk -F, "$16 #&732; /DX/" >temp.data

# filter out useless columns
FEATURE_PATTERN='phone, spk_id, error, word'
COLUMN_INDEX='$16","$8","$14","$19'
# filter out the lines with value 'DX' at the column 'Phone' ($16 in sm_train.data)
cat ../data_old/sm_train.data | sed '/!/d' | awk -F, "{print $COLUMN_INDEX}" \
	| sed '/^DX/d' >train_word.csv

cat train_word.csv | awk -F, '{print $3","$4}' | uniq -i >train_word_tmp.csv


