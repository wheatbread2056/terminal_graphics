# terminal_graphics version 0.2c
# a simple way to show graphics in the terminal, using only text characters and colors

from colorama import Fore as f, Back as b, just_fix_windows_console
import time
import os
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

def plot(x,y,c): # modify a pixel on the screen to a specific color (0-16) or -1 for nothing
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
        TSCREEN[y][i] = t[a]
        CSCREEN[y][i] = c
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

def draw(clr=True): # draw to the screen
    if clr == True:
        print('\033[A'*sy)
    for i in range(sy):
        p = ''
        for j in range(sx):
            if SCREEN[i][j] == -1:
                p+=' '
            else:
                p+=bc[SCREEN[i][j]]+c[CSCREEN[i][j]]+TSCREEN[i][j]
        print(p+c[0]+bc[0])
