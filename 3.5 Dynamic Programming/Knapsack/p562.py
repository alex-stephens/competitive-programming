# Competitive Programming 3
# Problem 562

T = int(input())

for _ in range(T):
    N = int(input())
    coins = sorted([0] + [int(x) for x in input().split()])
    N = len(coins) - 1
    #print(coins)
    W = sum(coins) // 2
    m = [[0 for _ in range(W+1)] for _ in range(N+1)]

    maxValue = 0    
    for c in range(1,N+1):
        for w in range(W+1):
            if coins[c] > w:
                m[c][w] = m[c-1][w]
            else:
                m[c][w] = max(m[c-1][w], coins[c] + m[c-1][w - coins[c]])
        maxValue = max(maxValue, max(m[c]))
    
    print(sum(coins) - 2*maxValue)