# Competitive Programming 3
# Problem 10258

import operator

N = int(input())
line = input()

for t in range(N):
    if t > 0: print('')
    line = input()
    entries = []

    done = False
    
    while line != '':
        C, P, T, L = line.split()
        C, P, T = int(C), int(P), int(T)
        entries.append([C, P, T, L])
        
        if t == N-1:
            try: line = input()
            except EOFError:
                break
        else: 
            line = input()
    
    contestants = set([entries[i][0] for i in range(len(entries))])
    maxC = max(contestants)
    
    score = {x:0 for x in contestants}
    solved = [set() for x in range(maxC+1)]
    penalty = [dict() for x in range(maxC+1)]
    
    for i in range(len(entries)):
        C, P, T, outcome = entries[i]
        if outcome == 'C' and P not in solved[C]:       # solved new problem
            score[C] += T
            if P in penalty[C]: score[C] += penalty[C][P]
            solved[C].add(P)
        
        elif outcome == 'I' and P not in penalty[C]:    # first penalty
            penalty[C][P] = 20
            
        elif outcome == 'I':                            # additional penalty
            penalty[C][P] += 20
    
    result = [[C, len(solved[C]), score[C]] for C in contestants]
    result.sort(key = operator.itemgetter(0))               # contestant num
    result.sort(key = operator.itemgetter(2))               # penalty
    result.sort(key = operator.itemgetter(1), reverse=True) # problems
    
    for i in range(len(contestants)):
        print(*result[i])
    