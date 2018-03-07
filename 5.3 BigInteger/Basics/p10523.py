# Competitive Programming 3
# Problem 10523

while True:
    try: 
        N, A = [int(x) for x in input().split()]
    except EOFError:
        break
    
    ans = sum([i * (A ** i) for i in range(1,N+1)])
    print(ans)
