import numpy as np
import pygame as pg
from pygame import surfarray,mouse
import time, random, math

x1 = -2
x2 = 1
y1 = -1
y2 = 1
rx = x2-x1
ry = y2-y1


w = 600
h = round(ry*(w/rx))

pg.init()
screen = pg.display.set_mode((w,h))
image = np.zeros((w,h,3))


def cell_to_pos(x,y):
    x = x1+x*(rx/w)
    y = y1+y*(ry/h)
    return (x,y)

def makepixels():
    pixels = []
    for y in range(h):
        pixels.append([complex(0,0) for _ in range(w)])
    return pixels

def draw(pixels):
    surfarray.blit_array(screen,image)
    pg.display.update()

def next(pixels):
    def iterate(value,x,y):
        x,y = cell_to_pos(x,y)
        value += complex(x,y)
        value **= 2
        return value
    
    for y in range(h):
        for x in range(w):
            if abs(pixels[y][x]) < 2:
                pixels[y][x] = iterate(pixels[y][x],x,y)
            elif image[x,y].all() == 0:
                changepixel(x,y)
    return pixels

def changepixel(x,y):
    image[x,y] = colour

def crop():
    global x1,x2,y1,y2,rx,ry,screen,w,h
    nx1,ny1 = mouse.get_pos()
    while mouse.get_pressed()[0] and running():
        x,y = mouse.get_pos()
        pg.draw.rect(screen,(255,255,255),(nx1,ny1,x-nx1,y-ny1))
        pg.display.update()
    x1,y1 = cell_to_pos(nx1,ny1)
    x2,y2 = cell_to_pos(x,y)
    
    rx = x2-x1
    ry = y2-y1

    print(rx,ry)
    if rx>ry:
        w = 500
        h = round(ry*(w/rx))
    else:
        h = 500
        w = round(rx*(h/ry))
    #if w<150: w = 150
    #if h<150: h = 150

    


#################################################





pixels = makepixels()
def running():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
    return True

iteration = 1
while running():
    colour = (140-115*math.cos((iteration-5)*0.02),140-115*math.cos((iteration-3)*0.04),140-115*math.cos((iteration+5)*0.06))
    if mouse.get_pressed()[0]:
        crop()
        pg.quit()
        pg.init()
        screen = pg.display.set_mode((w,h))
        pixels = makepixels()
        image = np.zeros((w,h,3))
        iteration = 1
    print(iteration)
    next(pixels)
    draw(pixels)
    iteration += 1