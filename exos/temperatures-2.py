import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526
temps = [int(temp) for temp in temps.split()]

if n == 0:
    print(0)
else:
    temp_ref = temps[0];
    for temp in temps:
        if abs(temp) < abs(temp_ref):
            temp_ref = temp
        elif abs(temp) == abs(temp_ref) and temp > 0:
            temp_ref = temp;
    print(temp_ref)
