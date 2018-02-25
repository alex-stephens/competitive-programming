# Competitive Programming 3
# Problem 195

from itertools import permutations

T = int(input())

for _ in range(T):
    string = list(input())

    sortedString = ['0'] * len(string)
    j = 0
    for i in range(26):
        cur = chr(ord('A') + i)
        for _ in range(string.count(cur)):
            sortedString[j] = cur
            j += 1
        cur = chr(ord('a') + i)
        for _ in range(string.count(cur)):
            sortedString[j] = cur
            j += 1
    
    for p in permutations(sortedString):
        print(''.join(p))