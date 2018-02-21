# Competitive Programming 3
# Problem 978

# note - this code is for testing only, does not use appropriate datastructure
# for fast insertion/deletion

T = int(input())

for t in range(T):
    B, SG, SB = [int(x) for x in input().split()]
    
    green, blue = [0 for _ in range(SG)], [0 for _ in range(SB)]
    for i in range(SG): green[i] = int(input())
    for i in range(SB): blue[i] = int(input())
    
    green.sort(reverse=True)
    blue.sort(reverse=True)
    
    
    while SB > 0 and SG > 0:
        numFights = 0
        for i in range(B):
            if i + 1 > SB or i + 1 > SG: break
            numFights += 1
        
            fight = min(green[i], blue[i])
            green[i], blue[i] = green[i] - fight, blue[i] - fight
        
        for i in range(numFights-1,-1,-1):
            if green[i] == 0: 
                green.pop(i)
                SG -= 1
            if blue[i] == 0: 
                blue.pop(i)
                SB -= 1
    
        green.sort(reverse=True)
        blue.sort(reverse=True)
            
    if len(blue) == 0 and len(green) == 0:
        print("green and blue died")
    elif len(blue) == 0:
        print("green wins")
        print(*green, sep='\n')
    else:
        print("blue wins")
        print(*blue, sep='\n')
        
    if t < T-1: print('')
        
    