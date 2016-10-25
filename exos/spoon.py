import sys
import math

def right_node(nodes, x, y):
    """ find the first right node
    and returns its position """
    try:
        return str(nodes.index('0', x+1)) + " " + str(y) + " " 
    except(KeyError, ValueError):
        return '-1 -1 '


def bottom_node(nodes, y, x):
    """ find the first right node
    and returns its position """
    try:
        return str(x) + " " + str(nodes.index('0', y+1))
    except(KeyError, ValueError):
        return '-1 -1 '

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

#print(width, height, file=sys.stderr)
nodes = []

for row in range(height):
    line = input()  # width characters, each either 0 or .
    nodes.append(list(line))

for i, row in enumerate(nodes):
    for j, cell in enumerate(row):
        if cell == '0':
            res = ""
            res += str(j) + " " + str(i) + " " #the node's position x y
            res += right_node(row, j, i)
            res += bottom_node([nodes_x[j] for nodes_x in nodes], i, j)
            print(res)
