# Competitive Programming 3
# Problem 10172

T = int(input())

for _ in range(T):
    N, S, Q = [int(x) for x in input().split()]
    
    queues = [[] for _ in range(N+1)]
    todo = 0
    
    for n in range(1,N+1):
        line = [int(x) for x in input().split()]
        todo += line.pop(0)
        queues[n] = line

    cargo = []
    pos, time, numCargo = 1, 0, 0

    while True:
        
        # unloading
        while numCargo > 0: 
            
            # unloaded to platform A
            if cargo[-1] == pos: 
                cargo.pop()
                numCargo -= 1
                todo -= 1
                failed = False
                time += 1
                continue
            
            # added to queue on platform B    
            if len(queues[pos]) < Q and numCargo > 0: 
                queues[pos].append(cargo.pop())
                numCargo -= 1
                failed = False
                time += 1
                continue
                
            break # if neither succeeded, unloading is done
         
        # loading
        while numCargo < S and len(queues[pos]) > 0:
            cargo.append(queues[pos].pop(0))
            numCargo += 1
            time += 1
            
        if todo == 0: break
    
        time += 2
        pos = pos + 1 if pos < N  else 1  # update and wraparound
    print(time)        