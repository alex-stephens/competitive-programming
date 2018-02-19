# Competitive Programming 3
# Problem 11517

from math import inf

T = int(input())

for _ in range(T):
    V = int(input())
    
    n = int(input())
    notes = [0 for _ in range(n)]

    for i in range(n):
        notes[i] = int(input())
        
    notes.sort()
    
    # number of bills required to make value x
    dp = [inf for _ in range(sum(notes) + 1)]
    dp[0] = 0
    
    for j in range(n):
        note = notes[j]
        for i in range(sum(notes[:j]), -1, -1):
            if dp[i] != inf:
                dp[i+note] = min(dp[i+note], dp[i] + 1)
        
    i = V
    while True:     
        if dp[i] != inf:
            print(i, dp[i])
            break
        i += 1        
