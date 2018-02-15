# Competitive Programming 3
# Problem 357

coins, C = [1, 5, 10, 25, 50], 5;
coins = [0] + coins

while True:
    try:
        N = int(input())
    except EOFError:
        break
    
    ways = [[0 for _ in range(N+1)] for _ in range(C+1)]
    for n in range(N+1):
        ways[1][n] = 1

    for c in range(C+1):
        ways[c][0] = 1

    
    for c in range(2,C+1):
        for n in range(1,N+1):
            
            ways[c][n] = ways[c-1][n] 
            if n >= coins[c]:
                ways[c][n] += ways[c][n-coins[c]]
                
    num = ways[-1][N]
    if num <= 1:
        print("There is only 1 way to produce {} cents change.".format(num))
    else:
        print("There are {} ways to produce {} cents change.".format(num, N))
