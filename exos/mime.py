import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

dico = dict()
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dico[ext.lower()] = mt
    
print(repr(dico), file=sys.stderr)
for i in range(q):
    fname = input()  # One file name per line.
    chops = fname.split('.')
    if len(chops) < 2: 
        print("UNKNOWN")
        continue
    
    try:
        print(chops, file=sys.stderr)
        print(dico[chops[-1].lower()])
    except IndexError:
        print("index error", file=sys.stderr)
        print("UNKNOWN")
    except KeyError:
        print("key error", file=sys.stderr)
        print("UNKNOWN")
