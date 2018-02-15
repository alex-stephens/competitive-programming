# Competitive Programming 3
# Problem 735

from bisect import bisect_left

scores = sorted([x for x in range(1,21)] + [2*x for x in range(1,21)] \
                 + [3*x for x in range(1,21)] + [0] + [50])
scores = list(set(scores))
length = len(scores)
print(scores)

while True:
    N = int(input())
    if N < 0: 
        print("END OF OUTPUT")
        break

    permutations, combinations = 0, 0

    for i in scores:
        for j in scores:
            target = N - i - j
            index = bisect_left(scores,target)
            if index > length - 1:
                continue
            k = scores[index]
            
            if k == target:
                permutations += 1
                
            if k == target and i >= j and j >= k:
                combinations += 1
    
    if permutations == 0:
        print("THE SCORE OF {} CANNOT BE MADE WITH THREE DARTS.".format(N))
    else:
        print("NUMBER OF COMBINATIONS THAT SCORES {} IS {}.".format(N,combinations))
        print("NUMBER OF PERMUTATIONS THAT SCORES {} IS {}.".format(N,permutations))
                
    print('***********************************',end='')
    print('***********************************')
        

