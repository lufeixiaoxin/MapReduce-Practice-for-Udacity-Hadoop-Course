#!/usr/bin/python

import sys

def reducer():
	
	prevPost = None
	students = []

	for line in sys.stdin:
		thisPost, thisStudent = line.strip().split('\t')

		if prevPost and thisPost != prevPost:
			print prevPost + '\t' + str(students)
			students = []

		students.append(int(thisStudent))
		prevPost = thisPost

	if prevPost:
		print prevPost + '\t' + str(students)

reducer()
