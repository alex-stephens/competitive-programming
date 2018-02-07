# Competitive Programming 3
# Problem 12356

while True:
    S, B = [int(x) for x in input().split()]
    if S == 0 and B == 0: break
    
    # ignore element 0, just there to fix indexing
    left, right = [x-1 for x in range(S+1)], [x+1 for x in range(S+1)]
    
    left[0], left[-1], right[0], right[-1] = 0, 0, 0, 0
    
    for _ in range(B):
        # range to delete
        L, R = [int(x) for x in input().split()]
        left[right[R]] = left[L]
        right[left[L]] = right[R]
                
        if left[L] == 0: print('*',end=' ')
        else: print(left[L], end=' ')
    
        if right[R] == 0: print('*')
        else: print(right[R])
    
    
    print('-')  