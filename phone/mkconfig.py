#! /opt/python/3.3/bin/python3
import configparser
import sys, os
import string

def main():
	if len(sys.argv) != 2:
		sys.exit("[USAGE] python mkconfig.py <fscore> or <kappa>")
	elif sys.argv[1] in ['fscore', 'kappa']:
		flag = sys.argv[1]
	else:
		sys.exit("Please input either <fscore> or <kappa>")

	conf = configparser.RawConfigParser()
	conf.add_section('General')
	conf.add_section('Input')
	conf.add_section('Tuning')
	conf.add_section('Output')

	conf.set('General', 'task', 'cross_validate')
	learners = '["RandomForestClassifier", "SVC", "LogisticRegression", "LinearSVC", "DecisionTreeClassifier", "GradientBoostingClassifier"]'
	conf.set('Input', 'learners', learners)
	conf.set('Input', 'suffix', '.jsonlines')
	conf.set('Tuning', 'grid_search', 'true')
	conf.set('Tuning', 'feature_scaling', 'both')

	if flag == 'fscore':
		conf.set('General', 'experiment_name', 'Pilot_fscore')
		conf.set('Tuning', 'objective', 'f1_score_micro')
	elif flag == 'kappa':
		conf.set('General', 'experiment_name', 'Pilot_kappa')
		conf.set('Tuning', 'objective', 'unweighted_kappa')

	with open("phone.lst", "r") as fp:
		phones = fp.readlines()

	tmp_dir = "./config/"
	if not os.path.exists(tmp_dir):
		os.makedirs(tmp_dir)
	for line in phones:
		ph = line.rstrip()

		output = "{}crossvalid_{}_{}.cfg".format(tmp_dir, ph, flag)
		print(output)
		with open(output, "w") as fw:
			conf.set('Input', 'train_location', './train/{}'.format(ph))
			conf.set('Input', 'featuresets', '[["{}"]]'.format(ph))
			conf.set('Output', 'results', 'output/{}'.format(ph))
			conf.set('Output', 'log', 'output/{}'.format(ph))
			conf.set('Output', 'predictions', 'output/{}'.format(ph))
			conf.write(fw)


if __name__ == '__main__':
	main()
