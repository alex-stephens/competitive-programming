# Competitive Programming 3
# Problem 11242

T = 1
while True:
    line = input()
    if line == '0':
        break
    else:
        f, r = [int(x) for x in line.split()]
        
    front = [int(x) for x in input().split()]
    rear =  [int(x) for x in input().split()]
    ratio = [0 for _ in range(f*r)]
    n = 0
    
    for i in range(f):
        for j in range(r):
            ratio[n] = rear[j] / front[i]
            n += 1
            
    ratio.sort()
    maxSpread = ratio[1] - ratio[0]
    for i in range(1,f*r):
        maxSpread = max(maxSpread, ratio[i]/ratio[i-1])
    print('{0:.2f}'.format(maxSpread))
