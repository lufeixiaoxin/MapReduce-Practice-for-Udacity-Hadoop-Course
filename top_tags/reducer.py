#!/usr/bin/python

import sys
from heapq import heappush, heappop, heappushpop

def reducer():
	
	prevTag = None
	count = 0
	pq = []

	for line in sys.stdin:

		thisTag = line.strip()

		if prevTag and thisTag != prevTag:
			if len(pq) < 10:
				heappush(pq, (count, prevTag))
			else:
				heappushpop(pq, (count, prevTag))	
			count = 0

		count += 1
		prevTag = thisTag

	if len(pq) < 10:
		heappush(pq, (count, prevTag))
	else:
		heappushpop(pq, (count, prevTag))

	ls = []
	while len(pq) > 0:
		item = heappop(pq)
		ls.append(item[1] + '\t' + str(item[0]))

	for i in range(len(ls)-1, -1, -1):
		print ls[i]


reducer()


