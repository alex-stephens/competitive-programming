# Competitive Programming 3
# Problem 441

from itertools import combinations

n = 1
while True:
    line = input()
    if line == '0': break
    if n > 1: print('')

    S = [int(x) for x in line.split()]
    k = S.pop(0)

    for c in combinations(S, 6):
        print(*c)         
    
    n += 1