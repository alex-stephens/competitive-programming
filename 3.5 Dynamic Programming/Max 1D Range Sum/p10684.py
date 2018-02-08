# Competitive Programming 3
# Problem 10684

while True:
    N = int(input())
    if N == 0: break

    count = 0
    seq = []
    while count < N:
        line = [int(x) for x in input().split()]
        count += len(line)
        seq += line

    curMax = 0;
    for i in range(N):
        curMax = max(curMax + seq[i], 0)
    
    if curMax > 0:
        print("The maximum winning streak is " + str(curMax) + ".")
    else:
        print("Losing streak.")
    
    
    