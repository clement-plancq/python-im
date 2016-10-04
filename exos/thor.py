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
    if LX > TX and LY < TY:
        TX = TX + 1
        TY = TY - 1
        print("NE")
    
    elif LX > TX and LY > TY:
        TX = TX + 1
        TY = TY + 1
        print("SE")
    
    elif LX < TX and LY < TY:
        TX = TX - 1
        TY = TY - 1
        print("NW")
    
    elif LX < TX and LY > TY:
        TX = TX - 1
        TY = TY + 1
        print("SW")
    
    elif LX > TX:
        TX = TX + 1
        print("E")
    
    elif LX < TX:
        TX = TX - 1
        print("W")
    
    elif LY < TY:
        TY = TY - 1
        print("N")
    
    elif LY > TY:
        TY = TY + 1;
        print("S");
    
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    #print("SE") # A single line providing the move to be made: N NE E SE S SW W or NW
