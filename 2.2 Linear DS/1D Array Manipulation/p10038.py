# Competitive Programming 3
# Problem 10038

while True:
    try:
        arr = [int(x) for x in input().split()]
    except EOFError:
        break
    n = arr.pop(0)
    diffs = [0 for _ in range(n-1)]
    
    for i in range(1,n):
        diffs[i-1] = abs(arr[i] - arr[i-1])
        
    diffs.sort()
    jolly = 1
    
    for i in range(n-1):
        if diffs[i] != i+1:
            jolly = False
            break
    
    if jolly: print("Jolly")
    else:     print("Not jolly")