#!/bin/python

import sys
from heapq import heappush, heappop
highh = []
lowh = []
n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    bigger = smaller = None

    if len(lowh) == 0 or a_t < lowh[0]*-1:
        heappush(lowh, -1*a_t)
    else:
        heappush(highh, a_t)

    #rebalance
    difference = len(lowh) - len(highh)
    if difference > 0:
        bigger, smaller = lowh, highh
    elif difference < 0:
        bigger, smaller= highh, lowh
    if abs(difference) >=2:
        heappush(smaller, -1*heappop(bigger))

    difference = len(lowh) - len(highh)
    if difference > 0:
        print float(lowh[0]*-1)
    elif difference < 0:
        print float(highh[0])
    else:
        print float(((lowh[0]*-1) +  highh[0])/2.0)


