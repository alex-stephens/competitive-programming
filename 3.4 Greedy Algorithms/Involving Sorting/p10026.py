# Competitive Programming 3
# Problem 10026

# Probably not working due to float comparisons

cases = int(input())

for _ in range(cases):
    input()
    N = int(input())
    
    T, S = [], []
    for _ in range(N):
        t,s = [int(x) for x in input().split()]
        T.append(t)
        S.append(s)

    cost = [s/t for t,s in zip(T,S)]
    job = [x for x in range(1,N+1)]
    
    
    cost, job =  [list(x) for x in zip(*sorted(zip(cost, job), reverse=True))]
    curCost, curStart = 0, 0
    # loop through job and sort lexicographically
    for i in range(N):
        if cost[i] != curCost:
            job[curStart:i] = sorted(job[curStart:i])
            curStart, curCost = i, cost[i]
    job[curStart:] = sorted(job[curStart:])

    print(' '.join([str(x) for x in job]))

