# Competitive Programming 3
# Problem 10616

t = 1;
while True:
    [N, Q] = [int(x) for x in input().split()]
    if N == 0 and Q == 0: break
    print("SET {}:".format(t))
    
    numbers = [0 for _ in range(N)]
    for n in range(N):
        numbers[n] = int(input())
    
    for q in range(1,Q+1):
        [D, M] = [int(x) for x in input().split()]
        
        mod = sorted([numbers[i] % D for i in range(N)])
        mod.insert(0,0) # fix indexing issues
        
        ways = [[[0 for _ in range(M+1)] for _ in range(D)] for _ in range(N+1)]   
        
        # base cases: number of ways of choosing 1 of the first n elements to
        # get a d (mod D) value
        for n in range(1,N+1):
            for d in range(D):
                ways[n][d][1] = mod[:n+1].count(d) - (1 if d == 0 else 0)
        
        
        for n in range(2,N+1): # choosing 1 of the first n numbers
            for d in range(D):
                for m in range(2,min(M+1,n+1)):
                    modval = (d - mod[n]) % D
                    ways[n][d][m] = ways[n-1][modval][m-1] # use the current number
                    ways[n][d][m] += ways[n-1][d][m]       # don't use current number
        
        print("QUERY {}: ".format(q), end='')
        print(ways[N][0][M])
    t += 1