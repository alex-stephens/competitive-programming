# Competitive Programming 3
# Problem 10487

from bisect import bisect_left

T = 1
while True:
    N = int(input())
    if N == 0:
        break
    print("Case {}:".format(T))
    
    numbers = [0 for _ in range(N)]
    for i in range(N):
        numbers[i] = int(input())
        
    numbers.sort()
    
    M = int(input())
    for _ in range(M):
        m = int(input())

        best = numbers[0] + numbers[1] # max value
        bestDiff = abs(m - best)
            
        for i in range(N):
            jTarget = bisect_left(numbers, m - numbers[i])
            j = min(N-1,jTarget)
            if abs(m - numbers[i] - numbers[j]) < bestDiff and j != i:
                best = numbers[i] + numbers[j]
                bestDiff = abs(m - best)
            j = max(0,jTarget)
            if abs(m - numbers[i] - numbers[j-1]) < bestDiff and j-1 != i:
                best = numbers[i] + numbers[j-1]
                bestDiff = abs(m - best)
                
        
        print("Closest sum to {} is {}.".format(m,best))
    T += 1
    