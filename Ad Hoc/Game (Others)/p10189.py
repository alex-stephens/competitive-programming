# Competitive Programming 3
# Problem 10189

from itertools import product

num = 1
while True:
    n, m = [int(x) for x in input().split()]
    if n == 0 and m == 0: break
    if num != 1: print('')
    print('Field #' + str(num) +  ':')

    field = [[0 for _ in range(m)] for _ in range(n)]
    hints = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        line = input()

        for j in range(m):
            field[i][j] = (1 if line[j] == '*' else 0)
            if line[j] == '*':
                for x in range(max(0,i-1), min(n,i+2)):
                    for y in range(max(0,j-1), min(m,j+2)):
                        hints[x][y] += 1
    
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                print('*', end='')
            else:
                print(hints[i][j], end = '')
        print('')
    
    
    
    
    
    
    num += 1