# Competitive Programming 3
# Problem 616

while True:
    N = int(input())
    if N < 0: break

    print('{} coconuts, '.format(N), end='')
    works = False
    for p in range(int(N**0.5 + 0.5), 1, -1):
        works = True
        n = N
        
        for _ in range(p):
            take = n//p
            rem = n % p
            if rem != 1:
                works = False
                break
            else:
                n -= take + 1
            
        if n % p != 0:
            works = False
            
        if works: break
    
        
    if not works: print('no solution')
    else: print('{} people and 1 monkey'.format(p))

