# Competitive Programming 3
# Problem 11933

while True:
    n = int(input())
    if n == 0: break

    ab = [0, 0]
    mask = 1
    ind = 0   # 0 --> a, 1 --> b
    
    while mask <= n:
        if mask & n != 0:
            ab[ind] += mask
            ind = 1 - ind       # switch between a and b
            
        mask <<= 1
        
    print(*ab)