# Competitive Programming 3
# Problem 713

T = int(input())

for _ in range(T):
    a, b = [int(x) for x in input().split()]
    
    x = int(str(int(str(a)[::-1]) + int(str(b)[::-1]))[::-1])
    print(x)