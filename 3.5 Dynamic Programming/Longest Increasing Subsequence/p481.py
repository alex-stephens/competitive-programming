# Competitive Programming 3
# Problem 481

import bisect

numbers = [];

while True: 
    try:
        numbers.append(int(input()))
    except:
        break

L = [numbers[0]]
lastindex = [0]
backtrace = [0 for _ in range(len(numbers))]

# find LIS by tracking minimum end value of longest increasing subsequence 
# for different lengths
for n in range(1, len(numbers)):
    i = bisect.bisect_left(L, numbers[n])
    if i == len(L):
        L.append(numbers[n])
        backtrace[n] = lastindex[-1]
        lastindex.append(n)
    elif numbers[n] < L[i]:
        L[i] = numbers[n]
        backtrace[n] = lastindex[i-1]
        lastindex[i] = n
        
# trace backwards to construct the sequence    
i = lastindex[-1]
seq = []
for _ in range(len(L)-1,-1,-1):
    seq.append(numbers[i])
    i = backtrace[i]

print(len(L),'\n-', sep='')    
print(*seq[::-1], sep = '\n')
    
