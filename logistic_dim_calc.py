#!/usr/bin/env python
""" Calculates the correlation dimension of the logistic map
Based on: http://www.sciencedirect.com/science/article/pii/0167278983902981
And "Chaos in Dynamical Systems: Edward Ott" page 90-91.
Supports parrallel threads.

Output format:
result;epsilon used

Output should be plotted on a log/log graph to get the final result

Created on Jun 22, 2013

@author: Guy Sheffer <guy.sheffer at mail.huji.ac.il>
"""
from numpy import arange,absolute
import pylab
import math
import time
import random
import os
from multiprocessing import Pool

#variables
K  = 2000
RESULT_FILE_PATH="/tmp/result"
POINTS_SEPERATOR=";"


def iterate(r,x):
    return r*x*(1-x)

def iterateABunchList(x,r,n):
    returnValue = []
    offset = 300
    for i in range(0,n + offset):
        x=iterate(r,x);
        if i > offset:
            returnValue.append(x)
    return returnValue;

heaviside = lambda x: 0.5 if x == 0 else 0 if x < 0 else 1

def get_zi():
    r = 3.56994567 #
    x0= 0.3
    return iterateABunchList(x0,r,K)


def sumWorker(i,zi,K):
    sumP=0
    for j in range(0,K):
        sumP+=heaviside(varepsilon - absolute(zi[i] - zi[j]))
        
    return sumP

def corrlationDimensionCalc(varepsilon,K):
            
    zi = get_zi()
    K = len(zi)
    iterations = K**2
    print "iterations:" + str(iterations)
    
    count=0
    sumI = 0
    
    
    pool = Pool(processes=4)# start 4 worker processes
    for i in range(0,K/4):
        #quick and dirty 4 threads to calculate the sum of I(r,epsilon)
        result1 = pool.apply_async(sumWorker, [i*4,zi,K])
        result2 = pool.apply_async(sumWorker, [i*4 +1,zi,K])
        result3 = pool.apply_async(sumWorker, [i*4 +2,zi,K])
        result4 = pool.apply_async(sumWorker, [i*4 +3,zi,K])
        
        sumI+= result1.get() + result2.get() + result3.get() + result4.get()
        
        count+=1
        if count % 100 == 0:            
                print str(float((i*K*4))/iterations*100) + "%"
    
    c= float(1.0)/float(K**2*sumI)
    return math.log(c)

os.system("rm " + RESULT_FILE_PATH)
#calculate 100 points
for i in range(1,100):
    print "point:" + str(i)
    with open(RESULT_FILE_PATH,'a') as f:
        #varepsilon = 0.02
        varepsilon = 0.2/(i*0.9) #epsilon as defined in Ott, the distance between boxes
        result = corrlationDimensionCalc(varepsilon,K)
        f.write(str(result) + POINTS_SEPERATOR + str(varepsilon) + "\n")

print "done"

