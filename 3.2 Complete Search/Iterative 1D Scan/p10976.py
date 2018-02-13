# Competitive Programming 3
# Problem 927

while True:
    try:
        k = int(input())
    except EOFError:
        break
    
    y = k + 1
    solutions = []
    while (1/k - 1/y <= 1/(k+1)):
        if (k * y) % (y - k) == 0:
            
            x = (k * y) // (y - k)
            
            if x < y: break
            solutions.append((x,y))

        y += 1

    print(len(solutions))
    for i in range(len(solutions)):
        print("1/{} = 1/{} + 1/{}".format(k,solutions[i][0],solutions[i][1]))