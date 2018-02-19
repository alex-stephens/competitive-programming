# Competitive Programming 3
# Problem 216

from itertools import permutations

t = 1
while True:
    N = int(input())
    if N == 0: break

    x, y = [0 for _ in range(N)], [0 for _ in range(N)]
    for i in range(N):
        x[i], y[i] = [int(x) for x in input().split()]
    
    D = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            D[i][j] = ((x[i] - x[j])**2  + (y[i] - y[j])**2 ) ** (1/2)
            
            
    minDist = sum([sum(D[i]) for i in range(N)])
    numbers = [x for x in range(N)]
    
    for p in permutations(numbers):
        dist = 0
        for i in range(1,N):
            dist += D[p[i]][p[i-1]]
            
        if dist < minDist:
            path = p
            minDist = dist
            
    print('**********************************************************')
    print("Network #{}".format(t))
    for i in range(1,N):
        x1, y1, x2, y2 = x[path[i-1]], y[path[i-1]], x[path[i]], y[path[i]]
        d = ((x1-x2)**2 + (y1-y2)**2) ** (1/2)
        print("Cable requirement to connect ({},{}) ".format(x1,y1),end='')
        print("to ({},{}) is {:.2f} feet.".format(x2,y2,d+16))
    
    print("Number of feet of cable required is ", end='')
    print("{:.2f}.".format(minDist + 16 * (N-1)))
    
    t += 1