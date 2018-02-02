# Competitive Programming 3
# Problem 11100

while True:
    n = int(input())
    if n == 0:
        break
    
    notDone = n
    bags = sorted([int(x) for x in input().split()])
    
    vals = set(bags)
    maxCount = max([bags.count(x) for x in vals])
    print(max([bags.count(x) for x in vals]))
    
    '''
    counts = {x:bags.count(x) for x in vals}
    
    for _ in range(maxCount):
        for x in  counts:
            if counts[x] > 0:
                print(x, end = ' ')
                counts[x] -= 1
        print('')
    print('')
    '''
    
    '''
    while notDone > 0:
        i, prev,numBags = 0, 0, 0
        current = []
        for i in range(len(bags)-1, -1, -1):
            if prev == 0:
                prev = bags.pop(i)
                current.append(prev)
                notDone -= 1
                
            elif bags[i] < prev:
                prev = bags.pop(i)
                current.append(prev)
                notDone -= 1
            else:
                i += 1
            
        for x in current:
            print(str(x), end = ' ')
        print('')
                
    print('')
    '''     
    prev = 0
    curCount = 0
    lines = [list() for x in range(maxCount)]
    for i in range(len(bags)):
        curCount = curCount + 1 if bags[i] == prev else 0
        lines[curCount].append(bags[i])
        prev = bags[i]
    
    for L in lines:
        for x in L:
            print(str(x), end = ' ')
        print('')
    print('')
