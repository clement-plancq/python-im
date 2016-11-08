import sys
import math

## Solution https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1
## CP

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

xmin = 0
ymin = 0
xmax = w
ymax = h

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if 'U' in bomb_dir:
        ymax = y0
    if 'D' in bomb_dir:
        ymin = y0
    if 'L' in bomb_dir:
        xmax = x0
    if 'R'in bomb_dir:
        xmin = x0
    
    x0 = (xmin + xmax) // 2
    y0 = (ymin + ymax) // 2
    print(x0, y0)

    # the location of the next window Batman should jump to.
    #print("0 0")
