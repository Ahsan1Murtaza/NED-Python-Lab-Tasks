# 2.   A dartboard of radius 10 and the wall it is hanging on are represented using the two dimensional coordinate system, with the board’s center at coordinate (0; 0). Variables x and y store the x- and y-coordinate of a dart hit. Write an expression using variables x and y that evaluates to True if the dart hits (is within) the dartboard, and evaluate the expression for these dart coordinates:
# (a) (0; 0)
# (b) (10; 10) 
# (c) (6; 6)
# (d) (7; 8)


def within_board(x,y,r=10):
    return x**2+y**2 <=r**2 # checking if inside the circle or not

a=within_board(0,0)
print(a)
b=within_board(10,10)
print(b)
c=within_board(6,6)
print(c)
d=within_board(7,8)
print(d)
