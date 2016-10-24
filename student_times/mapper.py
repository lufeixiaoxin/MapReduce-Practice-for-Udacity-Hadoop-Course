#!/usr/bin/python

import sys
import csv

def mapper():	
	reader = csv.reader(sys.stdin, delimiter = '\t')
    next(reader, None)
        
	for line in reader:
        print line[3] + '\t' + str(int(line[8][11:13]))

mapper()
