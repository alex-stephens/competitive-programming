# Competitive Programming 3
# Problem 11926

while True:
    n, m = [int(x) for x in input().split()]
    if m == 0 and n == 0: break
    result = True

    free = [True for _ in range(1000000)]

    for _ in range(n):
        start, end = [int(x) for x in input().split()]
        for i in range(start, end):
            if not free[i]:
                result = False
                break
            else:
                free[i] = False
   
    for _ in range(m):
        start, end, x = [int(a) for a in input().split()]
        interval = 0
        while start + interval < 1000000 and result:
        
            for i in range(start+interval, min(end+interval, 1000000)):
                if not free[i]:
                    result = False
                    break
                else:
                    free[i] = False
            
            interval += x

            
    if result:
        print("NO CONFLICT")
    else:
        print("CONFLICT")
                                                                      
    