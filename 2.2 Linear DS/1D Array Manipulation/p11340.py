# Competitive Programming 3
# Problem 11340

from time import time

s = time()

T = int(input())
for _ in range(T):
    K = int(input())
    values = dict()
    for _ in range(K):
        line = input().split()
        values[line[0]] = int(line[1])
    
    cents = 0
    M = int(input())
    for _ in range(M):
        line = input()
        for x in line:
            if x in values:
                cents += values[x]
                
    print('%.2f' % (cents/100),'$', sep='')

print('time taken:', time() - s)
