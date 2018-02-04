# Competitive Programming 3
# Problem 11559

while True:
    try:
        N, B, H, W = [int(x) for x in input().split()]
    except EOFError:
        break
    
    minPrice = B + 1
    for _ in range(H):
        price = int(input())
        beds = [int(x) for x in input().split()]
        
        for a in beds:
            if a >= N:
                minPrice = min(minPrice, price * N)
    
    if minPrice <= B:
        print(minPrice)
    else:
        print('stay home')