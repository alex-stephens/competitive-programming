# Competitive Programming 3
# Problem 11240


T = int(input())

for _ in range(T):
    line = [int(x) for x in input().split()]
    length = line.pop(0)
    
    less = True  # true when searching for a number less than current end
    subseq = [line[0]]
    for i in range(1,length):
        if line[i] < subseq[-1] and less:
            subseq.append(line[i])
            less = not less
            
        elif line[i] > subseq[-1] and not less:
            subseq.append(line[i])
            less = not less
        
        elif line[i] > subseq[-1] and less:
            subseq[-1] = line[i]
        elif line[i] < subseq[-1] and not less:
            subseq[-1] = line[i]
    
    print(len(subseq))
