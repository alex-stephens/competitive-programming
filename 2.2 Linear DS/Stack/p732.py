# Competitive Programming 3
# Problem 732

from itertools import combinations

while True: 
    try:
        input1 = list(input())
        while input1 == []:
            input1 = list(input())
    except EOFError:
        break
    
    input2 = input()
    while input2 == '': input2 = list(input())
    length = len(input1)

    indices = [x for x in range(2*length)]
    
    print('[')
    
    for index in combinations(indices, length):
        success = True
        stack = []
        i1, i2 = 0, 0 # indices in strings 1 and 2
        stackSize = 0
        string1 = list(input1)

        push = [False] * 2*length
        for x in index:
            push[x] = True

        for j in range(2*length):
            
            if push[j]:                     # push onto stack
                stack.append(string1[i1])
                i1 += 1
                stackSize += 1
            
            elif stackSize == 0:            # no item to pop from stack
                success = False
                break
            
            else:                           # pop from stack
                c = stack.pop()
                stackSize -= 1

                if c != input2[i2]:
                    success = False
                    break
                i2 += 1
            
        if success and i2 == length:    # check i2 to make sure got to end
            for i in range(2*length):
                if push[i]: 
                    print('i', end='')
                else:
                    print('o', end='')
                if i != 2*length - 1: print(' ', end='')
            
            print('')
    print(']')

        