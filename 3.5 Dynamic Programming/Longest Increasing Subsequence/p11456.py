# Competitive Programming 3
# Problem 11456

import bisect

def bisect_left_descending(L, n):
    return len(L) - bisect.bisect_right(L[::-1], n)

T = int(input())

for _ in range(T):
    N = int(input())
    if N == 0: 
        print(0)
        continue
    numbers = [0 for _ in range(N)];
    for n in range(N):
        numbers[n] = int(input())
    numbers.reverse()
    
    LInc = [numbers[0]]
    LDec = [numbers[0]]
    lastIndexInc = [0]
    lastIndexDec = [0]
    backtraceInc = [0 for _ in range(len(numbers))]
    backtraceDec = [0 for _ in range(len(numbers))]
    LIS = [1] + [0 for _ in range(len(numbers)-1)]
    LDS = [1] + [0 for _ in range(len(numbers)-1)]
    #print(numbers)
    
    # find LIS by tracking minimum end value of longest increasing subsequence 
    # for different lengths
    for n in range(1, len(numbers)):
        i = bisect.bisect_left(LInc, numbers[n])
        LIS[n] = i + 1
        if i == len(LInc):
            LInc.append(numbers[n])
            backtraceInc[n] = lastIndexInc[-1]
            lastIndexInc.append(n)
        elif numbers[n] < LInc[i]:
            LInc[i] = numbers[n]
            backtraceInc[n] = lastIndexInc[i-1]
            lastIndexInc[i] = n
            
        i = bisect_left_descending(LDec, numbers[n])
        LDS[n] = i + 1
        if i == len(LDec):
            LDec.append(numbers[n])
            backtraceDec[n] = lastIndexDec[-1]
            lastIndexDec.append(n)
        elif numbers[n] > LDec[i]:
            LDec[i] = numbers[n]
            backtraceDec[n] = lastIndexDec[i-1]
            lastIndexDec[i] = n
            
            
    tot = [LIS[i] + LDS[i] - 1 for i in range(len(LIS))]
    #print("LIS =", LIS)
    #print("LDS =", LDS)
    #print(tot)
    print(max(tot))