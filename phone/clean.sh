#! /bin/bash

# filter out the lines with value 'DX' at the column 'Phone' ($16 in sm_train.data)
#cat sm_train.data | awk -F, "$16 #&732; /DX/" >temp.data

# filter out useless columns
FEATURE_PATTERN='spkid_word, phone, error, onsetV, full, cs_raw, logcs_dur, cs_dur, am_dur|am_raw, wrdIn, str, v, logcs_raw'
COLUMN_INDEX='$16","$14","$8"_"$19","$2","$3","$4","$5","$6","$11","$13","$17","$21","$22","$23'
cat ../sm_train.data | sed '/!/d' | awk -F, "{print $COLUMN_INDEX}" >train.data
#cat train.data | head -n 1 >feature_names
# filter out the lines with value 'DX' at the column 'Phone' ($16 in sm_train.data)
cat train.data | sed '/^DX/d' >train.csv
#cat feature_names feature_values >train.csv
rm train.data

cat ../phlist.lst | sed '/DX/d' >phone.lst

