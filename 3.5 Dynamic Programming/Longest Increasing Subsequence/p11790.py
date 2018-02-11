# Competitive Programming 3
# Problem 11790

T = int(input())
for t in range(1,T+1):
    N = int(input())
    
    height = [int(x) for x in input().split()]
    width = [int(x) for x in input().split()]
    
    inc = [width[i] for i in range(N)]
    dec = [width[i] for i in range(N)]
    
    for i in range(1,N):
        for j in range(i):
            if height[i] > height[j] and inc[i] < inc[j] + width[i]:
                inc[i] = inc[j] + width[i]
            if height[i] < height[j] and dec[i] < dec[j] + width[i]:
                dec[i] = dec[j] + width[i]
                
    maxInc, maxDec = max(inc), max(dec)
    print("Case {}. ".format(t), end='')
    if maxInc >= maxDec:
        print("Increasing ({}). Decreasing ({}).".format(maxInc,maxDec))
    else:
        print("Decreasing ({}). Increasing ({}).".format(maxDec,maxInc))