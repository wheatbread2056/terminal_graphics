# terminal_graphics version 0.2f
# a simple way to show graphics in the terminal, using only text characters and colors

from colorama import Fore as f, Back as b, just_fix_windows_console
import time
import os
import random
just_fix_windows_console()

sx, sy = 0, 0
SCREEN, TSCREEN, CSCREEN = [], [], [] # background color array, text array, and text color array
# 16 colors, 0 = reset, 1 = black, 2 = white, 3 = red, 4 = yellow, 5 = green, 6 = cyan, 7 = blue, 8 = magenta, 9-16 = light versions of colors
c = [f.RESET, f.BLACK, f.WHITE, f.RED, f.YELLOW, f.GREEN, f.CYAN, f.BLUE, f.MAGENTA, f.LIGHTBLACK_EX, f.LIGHTWHITE_EX, f.LIGHTRED_EX, f.LIGHTYELLOW_EX, f.LIGHTGREEN_EX, f.LIGHTCYAN_EX, f.LIGHTBLUE_EX, f.LIGHTMAGENTA_EX]
bc = [b.RESET, b.BLACK, b.WHITE, b.RED, b.YELLOW, b.GREEN, b.CYAN, b.BLUE, b.MAGENTA, b.LIGHTBLACK_EX, b.LIGHTWHITE_EX, b.LIGHTRED_EX, b.LIGHTYELLOW_EX, b.LIGHTGREEN_EX, b.LIGHTCYAN_EX, b.LIGHTBLUE_EX, b.LIGHTMAGENTA_EX]

def gen_screen(x,y): # clear the previous screen array and generate a new one
    global SCREEN; global TSCREEN; global CSCREEN; global sx; global sy
    sx, sy = x, y
    SCREEN, TSCREEN, CSCREEN = [], [], []
    for i in range(y):
        row = [1] * x  # create a new list for each row with initial value 1
        trow = [' '] * x
        crow = [2] * x
        SCREEN.append(row); TSCREEN.append(trow); CSCREEN.append(crow)

def plot(x,y,c): # modify a pixel on the screen to a specific color (0-16)
    global SCREEN
    if y < 0 or y > sy-1 or x < 0 or x > sx-1:
        print(f'attempted to plot at ({x},{y}) which is outside ({sx},{sy})')
    else:
        SCREEN[y][x] = c

def char(x,y,t,c): # plot a text character onto the screen
    if not len(t) == 1:
        print('cannot set char to a string unequal to 1 character')
    else:
        if y < 0 or y > sy-1 or x < 0 or x > sx-1:
            print(f'attempted to plot char at ({x},{y}) which is outside ({sx},{sy})')
        else:
            global TSCREEN
            global CSCREEN
            TSCREEN[y][x] = t
            CSCREEN[y][x] = c

def string(x,y,t,c): # puts a string on the screen
    global TSCREEN
    global CSCREEN
    a = 0
    for i in range(x,x+len(t)):
        char(i,y,t[a],c)
        a += 1

def rect(x1,y1,x2,y2,c): # draw a rectangle
    global SCREEN
    # comparison checks
    if x1 > x2:
        bx, sx = x1, x2
    else:
        bx, sx = x2, x1
    if y1 > y2:
        by, sy = y1, y2
    else:
        by, sy = y2, y1
    for i in range(sy, by+1):
        for j in range(sx, bx+1):
            plot(j, i, c)

def line(x1, y1, x2, y2, c):  # draw a line using Bresenham's line algorithm (thanks chatgpt)
    global SCREEN
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    if dy < dx:
        err = dx / 2.0
        y = y1
        for x in range(x1, x2 + sx, sx):
            plot(x, y, c)
            err -= dy
            if err < 0:
                y += sy
                err += dx
    else:
        err = dy / 2.0
        x = x1
        for y in range(y1, y2 + sy, sy):
            plot(x, y, c)
            err -= dx
            if err < 0:
                x += sx
                err += dy

def tri(x1,y1,x2,y2,x3,y3,c): # draw a triangle. way too many arguments
    line(x1,y1,x2,y2,c)
    line(x2,y2,x3,y3,c)
    line(x3,y3,x1,y1,c)

def draw(clr=True): # draw to the screen
    cur = 0 # current pixel
    if clr == True:
        print('\033[A'*sy)
    for i in range(sy):
        for j in range(sx):
            cur+=1
            if not cur > (sx*sy):
                print(bc[SCREEN[i][j]]+c[CSCREEN[i][j]]+TSCREEN[i][j],end='')
        print(bc[0],c[0])