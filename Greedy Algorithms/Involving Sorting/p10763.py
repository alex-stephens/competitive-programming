# Competitive Programming 3
# Problem 10763

while True:
    
    n = int(input())
    if n == 0:
        break
        
    students = []
    for _ in range(n):
        a,b = [int(x) for x in input().split()]
        students.append([a,b])

    if n % 2 != 0:
        print("NO")
        continue
        
    asc, des = [], []
    
    for i in range(n):
        if students[i][0] > students[i][1]:
            des.append(students[i])
        else:
            asc.append(students[i][::-1])
            
    asc.sort()
    des.sort()
    
    success = True
    if len(asc) != len(des):
        print("NO")
        continue
    for i in range(n//2):
        if asc[i] != des[i]:
            success = False
            break
    if success:
        print("YES")
    else:
        print("NO")
    
    
    
    
    
    