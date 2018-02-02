# Competitive Programming 3
# Problem 11292

while True:
    impossible = False
    n, m = [int(x) for x in input().split()]
    if m == 0 and n == 0:
        break
    elif m < n:
        impossible = True
    
    heads, heights = [], []
    
    for _ in range(n):
        heads.append(int(input()))
        
    for _ in range(m):
        heights.append(int(input()))
        
    if not impossible:
        heights.sort()
        heads.sort()
        i, j, ans = 0, 0, 0
        
        while i < n and not impossible:
            
            if heights[j] >= heads[i]:
                ans += heights[j]
                j += 1
                i += 1
                if j >= m and i >= n:
                    break
                elif j >= m:
                    impossible = True

            else:
                while heights[j] < heads[i]:
                    j += 1
                    if j >= m:
                        impossible = True
                        break
        
    if impossible:
        print('Loowater is doomed!')
    else: 
        print(ans)
            
    
    
    
    
