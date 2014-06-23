#! /opt/python/3.3/bin/python3

# coding: utf-8
## Description: plot the statistics of the training set in order to analyze
## imbalanced distribution for each phoneme.

import numpy as np
import matplotlib.pyplot as plt
import sys
import subprocess

def plt_overall():
	# Samples distribution of training set
	#status1, val1 = commands.getstatusoutput("cat ~/mispronDetection/phone/train/*/*.jsonlines | grep 'correct' | wc -l")
	val1 = subprocess.Popen(args="cat ~/mispronDetection/phone/train/*/*.jsonlines | grep 'correct' | wc -l", shell=True, stdout=subprocess.PIPE)
	val2 = subprocess.Popen(args="cat ~/mispronDetection/phone/train/*/*.jsonlines | grep 'error' | wc -l", shell=True, stdout=subprocess.PIPE)
	#status2, val2 = commands.getstatusoutput("cat ~/mispronDetection/phone/train/*/*.jsonlines | grep 'error' | wc -l")
	labels = 'Correct', 'Error'
	sizes = [int(val1.stdout.read()), int(val2.stdout.read())]
	#print sizes
	colors = ['yellowgreen', 'lightskyblue']
	explode = (0, 0.1)
	plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=90)
	plt.axis('equal')
	plt.title('Samples distribution of training set')
	plt.show()


def plt_phone():
	with open("phone.lst", "r") as f:
		phones = f.readlines()

	src = "./train/"
	stat_ph = {}
	x_corr = []
	x_err = []
	x_label = []
	for ph in phones:
		p = ph.rstrip()
		subdir = '{}{}/{}.jsonlines'.format(src, p, p)
		val_corr = subprocess.Popen(args="cat {} | grep 'correct' | wc -l".format(subdir), shell=True, stdout=subprocess.PIPE)
		val_err = subprocess.Popen(args="cat {} | grep 'error' | wc -l".format(subdir), shell=True, stdout=subprocess.PIPE)
		#status_err, val_err = commands.getstatusoutput("cat {} | grep 'error' | wc -l".format(subdir))
		stat_ph[p] = [int(val_corr.stdout.read()), int(val_err.stdout.read())]
		x_corr.append(int(val_corr.stdout.read()))
		x_err.append(int(val_err.stdout.read()))
		x_label.append(p)
	x = [stat_ph[key] for key in stat_ph]
	#x = np.array([stat_ph[key] for key in stat_ph])
	#print(x)
	#print(type(x))

	N = len(x)
	width = 0.35
	ind = np.arange(N)
	p1 = plt.bar(ind, x_corr, width, color='g')
	p2 = plt.bar(ind, x_err, width, color='r', bottom=x_corr)
	plt.ylabel('Count')
	plt.xlabel('Phonemes')
	plt.title('Histogram of correct and error counts for each phoneme')
	plt.xticks(ind+width/2.0, x_label)
	plt.yticks(np.arange(0, max([x+y for x, y in zip(x_corr, x_err)]), 300))
	plt.legend((p1[0], p2[0]), ('Correct', 'Error'))
	plt.show()

def main():
	plt_overall()
	#plt_phone()

if __name__ == '__main__':
	main()
