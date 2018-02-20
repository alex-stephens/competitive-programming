# Competitive Programming 3
# Problem 11286

while True:
    N = int(input())
    if N == 0: break

    hmap = {}    

    for _ in range(N):
        classes = tuple(sorted([int(x) for x in input().split()]))
        
        if classes in hmap:
            hmap[classes] += 1
        else:
            hmap[classes] = 1
       
    maxCount = max(hmap.values())
    print(maxCount * list(hmap.values()).count(maxCount))