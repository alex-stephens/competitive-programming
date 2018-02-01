# Competitive Programming 3
# Problem 11264

T = int(input())

def coinTypes(N, coins):
    ans = 0
    rem = N
    for C in coins[::-1]:
        used = False
        while C <= rem:
            rem -= C
            used = True
            #print('used ' + str(C))
        ans += 1 if used else 0
    return ans

for _ in range(T):
    
    n = int(input())
    coins = [int(a) for a in input().split()]
    
    val = 0
    maxCoins = 0
    
    for i in range(len(coins)):
        C = coins[i]
        numCoins = coinTypes(val + C,coins)
        if numCoins > maxCoins:
            val += C
            maxCoins = numCoins

    print(maxCoins)
