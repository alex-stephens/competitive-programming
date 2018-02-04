# Competitive Programming 3
# Problem 11507

while True:

    L = int(input())
    if L == 0: break

    bends = input().split()
    x, y, z = 1, 0, 0
    
    for string in bends:
        if string == 'No':
            continue
        if string == '+y':
            x, y, z = -y, x, z
        elif string == '-y':
            x, y, z = y, -x, z
        elif string == '+z':
            x, y, z = -z, y, x
        elif string == '-z':
            x, y, z = z, y, -x
        
    if sum([x,y,z]) < 0: print('-', end='')
    else:                print('+', end='')
        
    if   x != 0: print('x')
    elif y != 0: print('y')
    elif z != 0: print('z')
