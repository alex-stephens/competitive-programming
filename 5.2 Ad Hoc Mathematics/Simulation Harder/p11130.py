# Competitive Programming 3
# Problem 11130

from math import * 

while True:
    x, y, vel, angle, s = [int(x) for x in input().split()]
    if (x, y, vel, angle, s) == (0,0,0,0,0): break

    accel = - vel / s
    dist = vel * s + 0.5 * accel * s**2
    
    finalX = x/2 + dist * cos(radians(angle))
    finalY = y/2 + dist * sin(radians(angle))
    
    print(int(finalX/x), int(finalY/y))