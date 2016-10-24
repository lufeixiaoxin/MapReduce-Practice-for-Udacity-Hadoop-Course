#!/usr/bin/python

import sys
import csv

def mapper():

	reader = csv.reader(sys.stdin, delimiter = '\t')
	next(reader, None)

	for line in reader:
		if line[5] == 'question':
			tags = line[2].split(' ')
			for tag in tags:
				print tag

mapper()
