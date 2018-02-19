# Competitive Programming 3
# Problem 10496

T = int(input())

def tsp(pos, bitmask):
    # return to start
    if bitmask == ((1 << n) - 1):
        return dist[pos][0]
    
    # been computed before
    if memo[pos][bitmask] != -1:
        return memo[pos][bitmask]
    
    # find shortest path calculated from nxt location
    ans = 1 << 30
    for nxt in range(n):
        # next pos has not been visited yet
        if nxt != pos and not (bitmask & (1 << nxt)):
            ans = min(ans, dist[pos][nxt] + tsp(nxt,bitmask | (1 << nxt)))
                
    memo[pos][bitmask] = ans
    return ans

for _ in range(T):
    X, Y = [int(x) for x in input().split()]    # size
    x, y = [int(x) for x in input().split()]    # start
    
    n = int(input()) + 1 # account for adding the start point to the set
    xb, yb = [0 for _ in range(n)], [0 for _ in range(n)]
    xb[0], yb[0] = x, y
    for i in range(1,n):
        xb[i], yb[i] = [int(x) for x in input().split()]
    
    # max 10 beepers
    memo = [[-1 for _ in range(1<<11)] for _ in range(11)]
    
    
    dist = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = abs(xb[i] - xb[j]) + abs(yb[i] - yb[j])
            
    print("The shortest path has length", tsp(0,1))
