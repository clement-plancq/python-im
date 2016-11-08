import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

pieces = {
    0: {'TOP': None, 'LEFT': None, 'RIGHT': None}, 
    1: {'TOP': (0, 1), 'LEFT': (0, 1), 'RIGHT': (0, 1)},
    2: {'TOP': None, 'LEFT': (1, 0), 'RIGHT': (-1, 0)},
    3: {'TOP': (0, 1), 'LEFT': None, 'RIGHT': None},
    4: {'TOP': (-1, 0), 'LEFT': None, 'RIGHT': (0, 1)},
    5: {'TOP': (1, 0), 'LEFT': (0, 1), 'RIGHT': None},
    6: {'TOP': None, 'LEFT': (1, 0), 'RIGHT': (-1, 0)},
    7: {'TOP': (0, 1), 'LEFT': None, 'RIGHT': (0, 1)},
    8: {'TOP': None, 'LEFT': (0, 1), 'RIGHT': (0, 1)},
    9: {'TOP': (0, 1), 'LEFT': (0, 1), 'RIGHT': None},
    10: {'TOP': (-1, 0), 'LEFT': None, 'RIGHT': None},
    11: {'TOP': (1, 0), 'LEFT': None, 'RIGHT': None},
    12: {'TOP': None, 'LEFT': None, 'RIGHT': (0, 1)},
    13: {'TOP': None, 'LEFT': (0, 1), 'RIGHT': None}
    }

matrix = []
# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    matrix.append(line.split(" "))
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

#print(matrix, file=sys.stderr)
# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    coord = int(matrix[yi][xi])
    new_position = tuple([sum(x) for x in zip((xi, yi), pieces[coord][pos])])
    print(" ".join(str(x) for x in new_position))

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    #print("0 0")
