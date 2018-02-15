# Competitive Programming 3
# Problem 10855

while True:
    N, n = [int(x) for x in input().split()]
    if N == 0 and n == 0: break

    big = ['0'*N for _ in range(N)]
    small = ['0'*n for _ in range(n)]
    
    for i in range(N): big[i] = input()
    for i in range(n): small[i] = input()
        
    
    count = {0:0, 90:0, 180:0, 270:0}
    
    for i in range(N-n+1):
        for j in range(N-n+1):
            # correct orientation
            match = True
            for x in range(n):
                for y in range(n):
                    
                    if big[i+x][j+y] != small[x][y]:
                        match = False
                        break
                if not match: break
            if match: count[0] += 1
            
            # 90 degrees clockwise
            match = True
            for x in range(n):
                for y in range(n):
                    if big[i+x][j+y] != small[n-1-y][x]:
                        match = False
                        break
                if not match: break
            if match: count[90] += 1

            # 180 degrees clockwise
            match = True
            for x in range(n):
                for y in range(n):
                    if big[i+x][j+y] != small[n-1-y][n-1-x]:
                        match = False
                        break
                if not match: break
            if match: count[180] += 1

            # 270 degrees clockwise
            match = True
            for x in range(n):
                for y in range(n):
                    if big[i+x][j+y] != small[y][n-1-x]:
                        match = False
                        break
                if not match: break
            if match: count[270] += 1

    print(*[count[i] for i in range(0, 360, 90)])
                        
                    
                