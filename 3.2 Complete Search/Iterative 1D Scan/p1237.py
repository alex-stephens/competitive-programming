# Competitive Programming 3
# Problem 927

T = int(input())

for t in range(T):
    N = int(input())
    
    upper, lower = [0 for _ in range(N)], [0 for _ in range(N)]
    name = []
    
    for i in range(N):
        n, l, u = [x for x in input().split()]
        name.append(n)
        upper[i], lower[i] = int(u), int(l)

    Q = int(input())
    for _ in range(Q):
        P = int(input())
        ans = None
        
        for n in range(N):
            if P >= lower[n] and P <= upper[n]:
                if ans == None: # first solution
                    ans = name[n]
                else:           # second solution
                    ans = None
                    break
        
        if ans == None: print("UNDETERMINED")
        else: print(ans)
        
    if t < T-1:
        print('')