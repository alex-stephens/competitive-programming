# Competitive Programming 3
# Problem 12405

n = int(input())

for a in range(n):
    length = int(input())
    x = input()
    count = 0
    fertile = [True if x[i] == '.' else False for i in range(length)] 
    
    for i in range(1,len(fertile)):
        if fertile[i-1] == True:
            count += 1
            fertile[i-1:i+2] = [False, False, False]
            
            
    count += 1 if fertile[-1] == True else 0
    print('Case ' + str(a+1) + ': ' + str(count))