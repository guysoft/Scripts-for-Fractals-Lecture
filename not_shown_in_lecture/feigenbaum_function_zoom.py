#!/usr/bin/env python
""" Feigenbaum Function Zoom
Will genrate an animation of the Feigenbaum Function zooming showing its fractal behaviour
Was not shown in the lecutre because its bassed on initial conditions, and we are not sure what that means.

Created on Jun 22, 2013

@author: Guy Sheffer <guy.sheffer at mail.huji.ac.il>
"""
from numpy import arange
import pygame
from pygame.locals import *
from pygame.transform import scale
from pygame.rect import Rect
import time
import pylab
import math


def pygameInit():
    pygame.init()
    pygame.display.set_caption('Basic Pygame program')
    screen = pygame.display.set_mode((0, 0))
    SIZEX, SIZEY = screen.get_size() 
    #SIZEX=int(SIZEY/1.1618)
    #SIZEY = SIZEY-100
    screen.fill((255,255,255))
    pygame.display.flip()

def point(x,y):
    #currentImage = pygame.transform.scale(myimage, (width,height))
    #screen.blit(currentImage, Rect(x,y,x + width,y + height))
    pygame.draw.line(screen, 0, [x,y] ,[x,y])

def iterate(r,x):
    return r*x*(1-x)

def iterateABunch(x,r,n):
    for i in range(0,n):
        x=iterate(r,x);
        
    return x;

def normList(L, normalizeTo=1):
    '''normalize values of a list to make its max = normalizeTo'''

    vMax = max(L)
    return [ x/(vMax*1.0)*normalizeTo for x in L]

def normalize_min_max(L):
    ''' Normalize a list to be from -1 to 1'''
    minList = min(L)
    for index in range(0,len(L)-1):
        points[index] -= minList
    L =  normList(points)
    
    for index in range(0,len(points)-1):
        L[index] -= 1
    return L

    
    #print "i:" + str(i)
    #print "res:" + str(res)
    
    #point(x/float(SIZEX),y)

pylab.rcParams['figure.figsize'] = 8, 8#800x800
def pylabPlot(x,y):
    
    try:
        pylab.plot(x,y,"b")
    except ValueError:
        print len(x)
        print len(y)
        
    pylab.xlabel('$x_0$')
    pylab.ylabel('$x_{200}$')
    pylab.title(r'Feigenbaum attractor')
    
    #pylab.show()

r = 3.56994567187094490184200515138649893676
center = 0.475086493388
print iterateABunch(0.5,r,200)

def buildMap(start,end,step,frame):
    points=[]
    axis = arange(start,end,step)
    for i in range(len(axis)):
        if i % 1000 == 0:
            print float(i) / len(axis)
        res = iterateABunch(axis[i],r,200)
        points.append(res)
    pylab.ylim([start,end])
    pylab.xlim([start,end])
    pylabPlot(axis,points)
    filename= "foo_%05d.png" % (frame,)
    print filename
    pylab.savefig(filename , bbox_inches=0)

pylab.ylim([0,1])

start=0.0
end = 1.0
for i in range(0,1):
    pylab.clf()
    print "frame:" + str(i)
    print start
    print end
    buildMap(start,end,(end- start)/800,i)
    
    start = start + end/(i*r)/3
    end =  end -     end/(i*r)/3

#pygameInit()
#point(x,y)
#pygame.display.flip()

print "done"

