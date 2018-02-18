# Competitive Programming 3
# Problem 1225

T = int(input())

for _ in range(T):
    n = int(input())
    count = [0 for _ in range(10)]
    
    for i in range(1,n+1):
        for x in str(i):
            count[int(x)] += 1
            
    print(*count)
    