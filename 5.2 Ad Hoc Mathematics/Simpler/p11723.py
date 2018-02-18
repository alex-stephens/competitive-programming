# Competitive Programming 3
# Problem 11723

t = 1
while True:
    R, N = [int(x) for x in input().split()]
    if R == 0 and N == 0: break
    print("Case {}: ".format(t), end='')

    available = 27 * N
    if available < R:
        print("impossible")
    else:
        # requires one suffix for each time R exceeds N by a further N
        req = (R - 1) // N  
        print(req)
    
    t += 1