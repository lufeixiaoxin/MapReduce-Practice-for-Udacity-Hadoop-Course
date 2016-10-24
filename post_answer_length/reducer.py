#!/usr/bin/python

import sys

def reducer():
	
	prevPost = None
	qLen = None
	aLen = None
	aCount = None

	for line in sys.stdin:
		thisPost, thisType, thisLen = line.split('\t')

		if prevPost and thisPost != prevPost:
			if qLen:
				if aCount != 0:
					print prevPost + '\t' + str(qLen) + '\t' + str(aLen / aCount)
				else:
					print prevPost + '\t' + str(qLen) + '\t0'

		if thisType == 'A':
			qLen = int(thisLen)
			aLen = 0
			aCount = 0
		elif qLen:
			aLen += int(thisLen)
			aCount += 1

		prevPost = thisPost

	if prevPost and qLen:
		if aCount != 0:
			print prevPost + '\t' + str(qLen) + '\t' + str(aLen / aCount)
		else:
			print prevPost + '\t' + str(qLen) + '\t' + '0'

reducer()
