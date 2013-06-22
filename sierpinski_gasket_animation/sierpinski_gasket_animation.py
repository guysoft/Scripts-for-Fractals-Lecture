#!/usr/bin/env python
""" Sierpinski triangle animation
A Sierpinski triangle animation generator using pygame
Default image used is a cute cat found on the internet (public domain?)

Created on Jun 22, 2013

@author: Guy Sheffer <guy.sheffer at mail.huji.ac.il>
"""
import pygame
from pygame.locals import *
from pygame.transform import scale
from pygame.rect import Rect
import time
pygame.init()

pygame.display.set_caption('Basic Pygame program')


screen = pygame.display.set_mode((0,0))
SIZEX, SIZEY = screen.get_size() 
SIZEX=int(SIZEY/1.1618)
SIZEY = SIZEY-100
myimage = pygame.image.load("cute-cat23.jpg")

imagerect = myimage.get_rect()
  
def elementDraw(width,height,x,y):
  currentImage = pygame.transform.scale(myimage, (width,height))
  screen.blit(currentImage, Rect(x,y,x + width,y + height))
  #pygame.draw.polygon(screen, 0, [[x, y], [x, y+height], [x+width, y]], 0)
  
def draw(step,width,height,x,y):
      
      if step == 0 :
          elementDraw(width,height,x,y)
      else:
	for i in range(0,1):
          draw(step-1,width/2,height/2 ,x,y)
          draw(step-1,width/2,height/2 ,x+width/2,y)
          draw(step-1,width/2,height/2 ,x,y+height/2)
      
      print step
for i in range(0,8):
  screen.fill((255,255,255))
  draw(i,SIZEX,SIZEY,SIZEX/2,0)
  pygame.display.flip()
  if i == 0:
      time.sleep(5)
  time.sleep(4)
  
time.sleep(3600)
