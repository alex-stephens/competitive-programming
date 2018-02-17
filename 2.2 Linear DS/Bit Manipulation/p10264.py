# Competitive Programming 3
# Problem 10264

while True:
    try:
        N = int(input())
    except EOFError:
        break
    
    weight = [0 for i in range(2**N)]
    
    for i in range(2**N):
        weight[i] = int(input())
        
    def potency(i):
        mask = 1
        ans = 0
        for _ in range(N):
            j = i ^ mask
            ans += weight[j]
            mask <<= 1
        return ans
    
    maxPotency = potency(0) + potency(1)
    
    for i in range(0, 2**N):
        for j in range(N):
            maxPotency = max(maxPotency, potency(i) + potency(i ^ 1<<j))
        
    print(maxPotency)