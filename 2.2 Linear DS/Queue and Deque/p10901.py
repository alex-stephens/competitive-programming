# Competitive Programming 3
# Problem 10901

T = int(input())

for t in range(T):
    if t > 0: print('')
    n, t, m = [int(x) for x in input().split()]    
    
    queues = [[], []]   # left and right queues
    remaining = [0, 0]
    i = 0
    
    # stuff for remembering order to print
    times = [[], []]
    left = [0 for _ in range(m)]    # 0 for left, 1 for right
    
    for _ in range(m):
        line = input().split()
        if line[1] == 'left':
            queues[0].append(int(line[0]))
            remaining[0] += 1
        else:
            queues[1].append(int(line[0]))
            remaining[1] += 1
            left[i] = 1
        i += 1
            
    pos = 0 # 0 = left, 1 = right
    time = 0
    carrying = []

    while sum(remaining) > 0 or len(carrying) > 0:
        
        # unload all 
        while len(carrying) > 0:
            carrying.pop(0)
            
        # load all that can be loaded
        while len(queues[pos]) > 0 and len(carrying) < n:
            if time >= queues[pos][0]:
                carrying.append(queues[pos].pop(0))
                remaining[pos] -= 1
                times[pos].append(time+t)
            else:
                break
        
        # update time if required to wait
        allowedToMove = False
        if remaining[0] > 0:
            nextTime = queues[0][0]
            if time >= queues[0][0]: allowedToMove = True
        if remaining[1] > 0:
            if remaining[0] > 0: nextTime = min(nextTime, queues[1][0])
            else: nextTime = queues[1][0]
            if time >= queues[1][0]: allowedToMove = True

         
        # move to other side or wait                   
        if allowedToMove or len(carrying) > 0:
            time += t
            pos = 1 - pos
        else:
            time = nextTime
    
    for i in left:
        print(times[i].pop(0))
                
    
    

