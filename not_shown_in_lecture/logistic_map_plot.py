#!/usr/bin/env python
""" Plots a small example of the logistic map
Trasnlated to python from: 
https://www.khanacademy.org/cs/logistic-map/1060730277

Just a small example I wrote for myself

Created on Jun 22, 2013

@author: Guy Sheffer <guy.sheffer at mail.huji.ac.il>
"""
from numpy import arange
import pygame
from pygame.locals import *
from pygame.transform import scale
from pygame.rect import Rect
import time
pygame.init()
pygame.display.set_caption('Basic Pygame program')
screen = pygame.display.set_mode((400, 0))
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

def iterateABunch(r,n):
    x=0.5;
    for i in range(0,n):
        x=iterate(r,x);
        
    return x;
  
for r in arange(0,4,4.0/SIZEX):
    h=iterateABunch(r,1000);
    
    for n in range(0,100):
      
        h=iterate(r,h);
        
        point(r/4*SIZEX,h*SIZEY);
print "done"
pygame.display.flip()
time.sleep(3000)

