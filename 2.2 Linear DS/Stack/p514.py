# Competitive Programming 3
# Problem 514

while True: 
    N = int(input())
    if N == 0: break
    
    while True:
        A = [int(x) for x in input().split()]
        if A == [0]: break
        
        stack = []
        i = 0
       
        for n in range(1,N+1):  # incoming cars
            stack.append(n)
            
            while len(stack) > 0:
                if A[i] == stack[-1]:  # remove from stack while numbers match
                    stack.pop()
                    i += 1
                else:
                    break
        
        if i == N: print("Yes")
        else: print("No")
        
    print('')
        