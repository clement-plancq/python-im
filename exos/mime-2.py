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
    ext = chops[-1].lower() if len(chops) > 1 else None
    print(dico.get(ext, "UNKNOWN"))
