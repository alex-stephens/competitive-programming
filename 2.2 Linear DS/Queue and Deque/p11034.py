# Competitive Programming 3
# Problem 10901

T = int(input())
for _ in range(T):
    L, m = [int(x) for x in input().split()]    
    L *= 100
    
    queues = [[], []]   # left and right queues
    remaining = [0, 0]
    
    for _ in range(m):
        line = input().split()
        if line[1] == 'left':
            queues[0].append(int(line[0]))
            remaining[0] += 1
        else:
            queues[1].append(int(line[0]))
            remaining[1] += 1
            
    pos = 0 # 0 for left, 1 for right
    trips = 0
    carrying = 0
    
    while sum(remaining) > 0:
        
        # unload all
        carrying = 0
        if sum(remaining) == 0: break
    
        # load as many as possible
        while len(queues[pos]) > 0:
            if carrying + queues[pos][0] <= L:
                carrying += queues[pos].pop(0)
                remaining[pos] -= 1
            else: break
        
        # toggle pos and add a trip
        pos ^= 1
        trips += 1            
            
    print(trips)