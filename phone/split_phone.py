#! /opt/python/3.3/bin/python3
import sys 
import csv
import pdb
import string
import json
import os

def split_phoneme(train, phone):
	'''
	split training set for each phoneme and return a dict:
	{
		'AH': [
		{'y': 'correct', // target label
		 'id': xxx, // line number + spkid + word
		 'x': {'logcs_dur': xxx, 'am_dur': xxx, ...} //feature set  
		}, 
		...
		],
		...
	} 
	'''
	feature_names = ['onsetV', 'full', 'cs_raw', 'logcs_dur', 'cs_dur', 'am_dur', 
		'am_raw', 'wrdIn', 'str', 'v', 'logcs_raw']
	target_names = ['correct', 'error']

	with open(train, "r") as fh:
		data = csv.DictReader(fh, delimiter=',')

		with open(phone, "r") as fp:
			phones = fp.readlines()
		
		train_set = {ph.rstrip().upper(): [] for ph in phones}

		for line in data:
			feature = {
			'id': '{}_{}'.format(data.line_num-1, line['spkid_word']),
			'y': target_names[int(float(line['error']))],
			'x': {key: float(line[key]) for key in feature_names}
			}
			train_set[line['phone']].append(feature)	
	print('Writing training files...')
	
	output_dir = "./train/"
	for key in train_set:
		tmp_dir = output_dir + key
		if not os.path.exists(tmp_dir):
			os.makedirs(tmp_dir)
		fname_json = os.path.join(tmp_dir, (key+'.jsonlines'))
		print("<{}>".format(fname_json)) 
		
		with open(fname_json, "w") as fw:
			for jsonline in train_set[key]:
				fw.write('{}\n'.format(json.dumps(jsonline)))
	print('done')
	

def main():
	train = "train.csv"
	phone = "phone.lst"
	
	## prepare training set for each phoneme
	split_phoneme(train, phone)


if __name__ == '__main__':
	main()
