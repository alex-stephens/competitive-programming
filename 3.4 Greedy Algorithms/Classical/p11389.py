# Competitive Programming 3
# Problem 11389


while True:
    # number of routes, max per day, overtime rate
    n, d, r = [int(a) for a in input().split()]
    if n == 0 and d == 0 and r == 0:
        break
    
    morning = sorted([int(a) for a in input().split()])
    evening = sorted([int(a) for a in input().split()])[::-1]
    ans = 0
    for i in range(len(morning)):
        x = morning[i] + evening[i]
        if x > d:
            ans += x - d
    print(ans*r)