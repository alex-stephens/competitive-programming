# Competitive Programming 3
# Problem 927

T = int(input())

for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    
    count = 0
    
    for i in range(1,N):
        for j in range(i):
            count += 1 if A[i] >= A[j] else 0
            
    print(count)
            
    