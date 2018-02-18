# Competitive Programming 3
# Problem 10773

T = int(input())

for t in range(1,T+1):
    print("Case {}: ".format(t), end='')
    d, v, u = [int(x) for x in input().split()]
    
    if v >= u or v == 0:
        print("can't determine")   
    else:
        print("{:.3f}".format(d/((u**2 - v**2)**0.5) - d/u))
