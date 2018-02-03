# Competitive Programming 3
# Problem 11100

while True:
    n = int(input())
    if n == 0:
        break
    
    bags = sorted([int(x) for x in input().split()])
    
    vals = set(bags)
    maxCount = max([bags.count(x) for x in vals])
    print(max([bags.count(x) for x in vals]))

    lineToInsert = 0
    lines = [list() for x in range(maxCount)]
    
    for i in range(len(bags)):
        lines[lineToInsert].append(bags[i])
        lineToInsert += 1
        lineToInsert = 0 if lineToInsert > maxCount-1 else lineToInsert
            
    for L in lines:
        print(' '.join((str(x) for x in L)))
    print('')