# Competitive Programming 3
# Problem 11498

while True:
    N = int(input())
    if N == 0: break

    xd, yd = [int(x) for x in input().split()]
    
    for _ in range(N):
        x, y = [int(x) for x in input().split()]
        if x > xd and y > yd:
            print('NE')
        elif x < xd and y > yd:
            print('NO')
        elif x > xd and y < yd:
            print('SE')
        elif x < xd and y < yd:
            print('SO')
        else:
            print('divisa')