#! /opt/python/3.3/bin/python3
import csv
import string

def main():
	data_old = "./train_word.csv"
	with open(data_old, "r") as fd:
		data = csv.DictReader(fd, delimiter=',')

		train_set = {}
		prevLine = {'word': '', 'error': 0.0}
		for line in data:
			if (line['word'] != prevLine['word']):
				prevLine = line
			elif (line['error'] != prevLine['error']):
				prevLine['error'] = 1.0
			#elif (line['error'] == prevLine['error']):
			print(line)

			#feature = {
			#	'id': '{}_{}'.format(line['spkid'], line['phone']),
			#	'x': {line['word']: int(float(line['error']))},
			#	'y':
			#}




if __name__ == '__main__':
	main()
