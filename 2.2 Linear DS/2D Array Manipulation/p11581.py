# Competitive Programming 3
# Problem 11581

T = int(input())

def f(g):
    new = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i > 0: new[i][j] += grid[i-1][j]
            if j > 0: new[i][j] += grid[i][j-1]
            if i < 2: new[i][j] += grid[i+1][j]
            if j < 2: new[i][j] += grid[i][j+1]
            new[i][j] %= 2
    return new

for _ in range(T):
    input()
    grid = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        line = input()
        for j in range(3):
            grid[i][j] = int(line[j])
            
    for i in range(3):
        print(grid[i])
    new = f(grid)
    for i in range(3):
        print(new[i])
    print('')
            