# Competitive Programming 3
# Problem 11581

T = int(input())

def f(g):
    new = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i > 0: new[i][j] += g[i-1][j]
            if j > 0: new[i][j] += g[i][j-1]
            if i < 2: new[i][j] += g[i+1][j]
            if j < 2: new[i][j] += g[i][j+1]
            new[i][j] %= 2
    return new

# return interpretation of grid as binary value
def val(g):
    n = 2**8
    ans = 0
    for i in range(3):
        for j in range(3):
            ans += g[i][j] * n
            n //= 2
    return ans

for _ in range(T):
    input()
    g = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        line = input()
        for j in range(3):
            g[i][j] = int(line[j])
            
    seen = dict()
    count = -1 # initially have not shown i=0 is a solution
                
    while val(g) not in seen:
        seen[val(g)] = 1
        g = f(g)
        count += 1

    # subtract 1 to get the last index where it was finite
    print(count-1)
            