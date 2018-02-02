# Competitive Programming 3
# Problem 11389

n = 0
while True:
    n += 1

    B, S = [int(a) for a in input().split()]
    if B == 0 and S == 0:
        break
    
    bach, spin = [], []
    for _ in range(B):
        bach.append(int(input()))
        
    for _ in range(S):
        spin.append(int(input()))
        
    bach.sort()
    spin.sort()
    
    
    print('Case ' + str(n) + ':', end = ' ')
    
    print(max(0, B - S), end = '')
    if B > S:
        print(' ' + str(min(bach)))
    else:
        print('')
    