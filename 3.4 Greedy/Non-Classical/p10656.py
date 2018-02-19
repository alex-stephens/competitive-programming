# Competitive Programming 3
# Problem 10656

while True:
    N = int(input())
    if N == 0:
        break
    
    arr = []
    length = N
    for _ in range(N):
        arr.append(int(input()))
        
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            arr.pop(i)
            length -= 1
        
    if length == 0:
        print(0)
        continue
        
    for i in range(len(arr)):
        print(str(arr[i]), end = '')
        if i != len(arr) - 1:
            print(' ', end = '')
    print('')
            
        
        
