# Competitive Programming 3
# Problem 12321

while True:

    L, G = [int(x) for x in input().split()]
    if L == 0 and G == 0:
        break
    
    left, right = [], []
    for _ in range(G):
        x, r = [int(a) for a in input().split()]
        left.append(max(x-r,0))   # cut off negatives
        right.append(min(x+r,L))
        
    left, right = [list(x) for x in zip(*sorted(zip(left, right)))]
    
    curStart, curEnd, maxCovered = -1,0, -1
    num, failed = 0, False
    if min(left) > 0 or max(right) < L:
        failed = True
    
    for i in range(0,G):

        if left[i] > maxCovered and left[i] <= curEnd and right[i] > curEnd:
            maxCovered = curEnd
            curStart = left[i]
            curEnd = right[i]
            num += 1
            
        elif left[i] == curStart and right[i] > curEnd:
            curStart, curEnd = left[i], right[i]

        elif left[i] <= maxCovered and right[i] > curEnd:
            curStart, curEnd = left[i], right[i]
            
        if left[i] > curEnd and curEnd < L:
            failed = True
            break
        elif curEnd == L:
            break
        
    if failed or curEnd < L:
        print(-1)
    else:
        print(G - num)
    
        