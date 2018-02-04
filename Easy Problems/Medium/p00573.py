# Competitive Programming 3
# Problem 00573


while True:
    
    H, U, D, F = [int(x) for x in input().split()]
    if H == 0:
        break
    
    height, climb, fall, fatigue = 0, U, D, 0.01 * F * U
    day = 1

    while True:
        
        height += climb if climb > 0 else 0
        
        if height > H: break
        
        height -= fall
        if height < 0: break
    
        climb -= fatigue
        day += 1
    
    if height > H:
        print('success on day ' + str(day))
    else:
        print('failure on day ' + str(day))