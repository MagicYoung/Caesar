Based on SKLL wrapper

1. Description of files
clean.sh
split_phone.py
mkconfig.py
batch_run.sh
stats.py




phone: experiments based on phone-level features (11), such as,
['onsetV', 'full', 'cs_raw', 'logcs_dur', 'cs_dur', 'am_dur', 'am_raw', 'wrdIn', 'str', 'v', 'logcs_raw']




word:

2. processes of running experiments
./clean.sh


./split_phone.py ## prepare training samples for each phoneme

./mkconfig.py fscore
./mkconfig.py kappa

./batch_run.sh
