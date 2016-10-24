#!/usr/bin/python

import sys

def reducer():
	oldStudent = None
	oldHour = None
	countHour = [0] * 24
	count = 0

	for line in sys.stdin:
		thisStudent, thisHour = line.split('\t')
		if oldStudent and thisStudent != oldStudent:
			countHour[int(oldHour)] = count
			maxCount = max(countHour)
			for i in range(0,24):
				if countHour[i] != 0 and countHour[i] == maxCount:
					print oldStudent + '\t' + str(i)
			countHour = [0] * 24
			count = 0
			
		elif oldHour and thisHour != oldHour:
			countHour[int(oldHour)] = count
			count = 0

		count += 1
		oldStudent = thisStudent
		oldHour = thisHour

	if oldStudent:
		countHour[int(oldHour)] = count
		maxCount = max(countHour)
		for i in range(0,24):
			if countHour[i] != 0 and countHour[i] == maxCount:
				print oldStudent + '\t' + str(i)

reducer()
