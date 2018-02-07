# Competitive Programming 3
# Problem 00696

while True:
    m, n = [int(x) for x in input().split()]
    if m == 0 and n == 0: break
    
    if 0 in [m, n] or 1 in [m, n]:
        x = m * n
    elif m == 2 or n == 2:
        blocksOfFour = (max(m,n) + 2) // 4
        additional = max(2 * (max(m,n) - 4*blocksOfFour), 0)
        x = 4 * blocksOfFour + additional
    else:
        x = (m*n + 1) // 2
    print('{} knights may be placed on a {} row {} column board.'.format(x,m,n))