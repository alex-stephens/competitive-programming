# Competitive Programming 3
# Problem 10107

from bisect import bisect_left

numbers = []
length = 0

while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    length += 1
    i = bisect_left(numbers, n)g
    numbers.insert(i, n)
    
    if length % 2 == 1:
        print(numbers[length//2])
    else:
        print((numbers[length//2] + numbers[length//2 - 1])//2)
    
    