# Competitive Programming 3
# Problem 927

T = int(input())

for _ in range(T):
    c = [int(x) for x in input().split()]
    degree = c.pop(0)    # polynomial degree
    
    d = int(input())
    k = int(input())
    
    n = int( ((k/d)**0.5) / 2)
    while (n * (n+1)) / 2 < k/d:
        n += 1
    
    an = 0;
    for i in range(degree+1):
        an += c[i] * (n**i)
        
    print(an)
        