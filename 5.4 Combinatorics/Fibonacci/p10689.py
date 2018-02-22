# Competitive Programming 3
# Problem 10689

T = int(input())

period = {1:60, 2:300, 3:1500, 4:150000}

for _ in range(T):
    a, b, N, M = [int(x) for x in input().split()]
    
    p = period[M]
    cap = 10 ** (M)
    
    Nreduced = N % p
    
    fib = [a, b, 0]
    
    for n in range(2,Nreduced + 1):
        fib[n%3] = (fib[(n-1)%3] + fib[(n-2)%3]) % cap
        
    print(fib[Nreduced % 3])
