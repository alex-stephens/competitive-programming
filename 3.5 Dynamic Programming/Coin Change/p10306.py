# Competitive Programming 3
# Problem 10306

from math import inf

N = int(input())

for _ in range(N):
    line = input()
    while line == '': line = input()
    m, S = [int(x) for x in line.split()]
    coins = [[0,0] for _ in range(m+1)]
    
    for i in range(1,m+1):
        line = input()
        while line == '': line = input()
        
        coins[i] = [int(x) for x in line.split()]
        
    # minimum number of coins required to get each value combination
    A = [[inf for _ in range(S+1)] for _ in range(S+1)]
    A[0][0] = 0
    
    for i in range(S+1):
        for j in range(S+1):
            for coin in coins:
                if i >= coin[0] and j >= coin[1]:
                    A[i][j] = min(A[i][j], A[i-coin[0]][j-coin[1]] + 1)

    # Check each grid value and find the minimum one with correct e-modulus
    minCoins = inf
    for i in range(S+1):
        for j in range(S+1):
            if i**2 + j**2 == S**2:
                minCoins = min(minCoins, A[i][j])
    
    if minCoins == inf:
        print("not possible")
    else:
        print(minCoins)
        
    
    
