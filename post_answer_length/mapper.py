#!/usr/bin/python

import sys
import csv

def mapper():
	reader = csv.reader(sys.stdin, delimiter = '\t')
	next(reader, None)

	for line in reader:
		if line[5] == 'question':
			print line[0] + '\t' + 'A' + '\t' + str(len(line[4]))
		elif line[5] == 'answer':
			print line[6] + '\t' + 'B' + '\t' + str(len(line[4]))

mapper()
