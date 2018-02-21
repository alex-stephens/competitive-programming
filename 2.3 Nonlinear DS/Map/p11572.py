# Competitive Programming 3
# Problem 11572

T = int(input())

for _ in range(T):
    N = int(input())
    
    # 'length' is the length of the longest subsequence ending at current loc
    start, length, longest = 0, 0, 0
    hmap = {}
    
    for i in range(N):
        n = int(input())
        
        if n not in hmap or hmap[n] < start:
            hmap[n] = i
            length += 1
            
        else:
            longest = max(length, longest)
            length = i - hmap[n]
            start = hmap[n]
            hmap[n] = i
    
    print(max(length, longest))
