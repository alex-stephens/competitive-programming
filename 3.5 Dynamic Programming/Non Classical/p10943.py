# Competitive Programming 3
# Problem 10943

cap = 100

# dp[n][k] is the number of ways to get n using k integers
dp = [[0 for _ in range(cap+1)] for _ in range(cap+1)]

dp[0][0] = 1

for n in range(cap+1):
    dp[n][1] = 1

for k in range(2,cap+1):
    for n in range(cap+1):
        for i in range(n+1):
            dp[n][k] += dp[n-i][k-1]
            
while True:
    N, K = [int(x) for x in input().split()]
    if N == 0 and K == 0: break

    print(dp[N][K] % 1000000)