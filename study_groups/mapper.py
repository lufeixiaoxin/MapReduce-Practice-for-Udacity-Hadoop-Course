#!/usr/bin/python

import sys
import csv

def mapper():

	reader = csv.reader(sys.stdin, delimiter = '\t')
	next(reader, None)

	for line in reader:
        #if it's a parent node, print it's node id
		if line[6] == '\N':
			print line[0] + '\t' + line[3]
        #if  it's child node, print it's parent_id
		else:
			print line[6] + '\t' + line[3]


mapper()
