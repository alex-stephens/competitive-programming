# Competitive Programming 3
# Problem 507

T = int(input())

for t in range(1,T+1):
    
    r = int(input())
    
    if r <= 1:
        print("Route {} has no nice parts".format(t))
        continue
    
    niceness = [int(input()) for _ in range(r-1)]
            
    # score and length of best route ending at each index
    score, length = [0 for _ in range(r-1)], [0 for _ in range(r-1)]
    
    score[0] = max(0, niceness[0])
    length[0] = 1 if niceness[0] >= 0 else 0
    
    for i in range(1,r-1):
        score[i] = max(score[i-1] + niceness[i], 0)
        length[i] = length[i-1] + 1 if score[i] != 0 else 0
        
    bestScore = max(score)
    solutions = score.count(bestScore)
    bestSolIndex = score.index(max(score))
    longest = length[bestSolIndex]
    maxLength = 0
    #print(score)
    
    for i in range(0,r-1):
        if score[i] == bestScore and length[i] > longest:
            longest = length[i]
            bestSolIndex = i
    
    if bestScore > 0:
        print("The nicest part of route {} is between stops {} and {}"\
              .format(t, bestSolIndex - longest + 2, bestSolIndex+2))
    else:
        print("Route {} has no nice parts".format(t))
                
    
    

         