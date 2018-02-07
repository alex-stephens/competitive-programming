# Competitive Programming 3
# Problem 11172

N = int(input())

for _ in range(N):
    a, b = [int(x) for x in input().split()]
    if a > b:   print('>')
    elif a < b: print('<')
    else:       print('=')