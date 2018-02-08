# Competitive Programming 3
# Problem 00787


while True:
    try:
        numbers = [int(x) for x in input().split()]
    except EOFError:
        break
    
    numbers.pop(-1)
    length = len(numbers)
    
    lowest, highest = [0 for _ in range(length)], [0 for _ in range(length)]
    lowest[0], highest[0] = numbers[0], numbers[0]
    
    for i in range(1, length):
        if numbers[i] >= 0:
            lowest[i] = min(lowest[i-1]*numbers[i], numbers[i])
            highest[i] = max(highest[i-1]*numbers[i], numbers[i])
        else:
            lowest[i] = min(highest[i-1]*numbers[i], numbers[i])
            highest[i] = max(lowest[i-1]*numbers[i], numbers[i])
        
    print(max(highest))
        