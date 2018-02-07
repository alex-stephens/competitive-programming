# Competitive Programming 3
# Problem 10114

while True:
    duration, down, loan, lines = [float(x) for x in input().split()]
    duration, lines = int(duration), int(lines)
    if duration < 0: break

    carVal = loan + down
    owing = loan
    
    months, dep = [], []
    for _ in range(lines):
        m, d = [float(x) for x in input().split()]
        months.append(int(m))
        dep.append(d)
    
    
    for i in range(duration+1):
        if i in months:
            index = months.index(i)
            carVal *= 1 - dep[index]
            prev = dep[index]
        else:
            carVal *= 1 - prev
            
        owing = loan - i * (loan / duration)
        
        if owing <= carVal:
            break
        
    print(str(i), end = '')
    if i == 1: 
        print(' month')
    else:
        print(' months')
            
            
        
        
        
        
        
        