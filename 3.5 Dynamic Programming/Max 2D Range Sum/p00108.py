# Competitive Programming 3
# Problem 00108

while True:
    try: 
        N = int(input())
    except EOFError:
        break;

    count = 0
    seq = []
    while count < N**2:
        line = [int(x) for x in input().split()]
        count += len(line)
        seq += line

    #print(seq)
    
    grid = [[0 for _ in range(N)] for _ in range(N)]
    n = 0;
    for i in range(N):
        for j in range(N):
            grid[i][j] = seq[n]
            n += 1
    
    C = [[0 for _ in range(N)] for _ in range(N)]
    C[0][0] = grid[0][0]
    
    # base cases
    for i in range(1,N):
        C[i][0] = C[i-1][0] + grid[i][0]
    for j in range(1,N):
        C[0][j] = C[0][j-1] + grid[0][j]
    
    for i in range(1,N):
        for j in range(1,N):
            C[i][j] = grid[i][j] + C[i-1][j] + C[i][j-1] - C[i-1][j-1]
    
    ans = 0 
    for i in range(N):
        for j in range(N):
            for x in range(i,N):
                for y in range(j,N):
                    t1 = C[x][y]
                    t2 = C[i-1][y] if i > 0 else 0
                    t3 = C[x][j-1] if j > 0 else 0
                    t4 = C[i-1][j-1] if (i > 0 and j > 0) else 0
                    ans = max(ans, t1 - t2 - t3 + t4)

    print(ans)
    
        

            
       