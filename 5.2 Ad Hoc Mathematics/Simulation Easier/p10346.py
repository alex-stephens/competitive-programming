# Competitive Programming 3
# Problem 10346

while True:
    try: 
        n, k = [int(x) for x in input().split()]
    except EOFError:
        break
    
    butts = n    
    
    while butts >= k:
        new = butts // k
        n += new
        butts = butts % k + new
    print(n)