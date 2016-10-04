import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in input().split()]


# game loop
while 1:
    E = int(input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
    direction = ""
    
    if LY < TY:
        TY -= 1
        direction += "N"
    
    elif LY > TY:
        TY += 1
        direction += "S"
        
    if LX > TX:
        TX += 1
        direction += "E"
    
    elif LX < TX:
        TX -= 1
        direction += "W"
    
    print(direction)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    #print("SE") # A single line providing the move to be made: N NE E SE S SW W or NW
