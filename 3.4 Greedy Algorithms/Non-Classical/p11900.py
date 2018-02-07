# Competitive Programming 3
# Problem 11900

T = int(input())

for case in range(1,T+1):

    n, P, Q = [int(x) for x in input().split()]
    weights = sorted([int(x) for x in input().split()])
    
    num, total = 0, 0
    for i in range(n):
        if total + weights[i] <= Q and num + 1 <= P:
            num += 1
            total += weights[i]

    print('Case ' + str(case) + ': ' + str(num))