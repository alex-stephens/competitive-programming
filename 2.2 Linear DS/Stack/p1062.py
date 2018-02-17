# Competitive Programming 3
# Problem 1062

T = 1
while True: 
    string = list(input())
    if string == list('end'):
        break
    
    length = len(string)
    count = 0
    while length > 0:
        
        # calculate max value remaining at or after each index
        maxRem = ['0' for _ in range(length)]
        maxRem[-1] = string[-1]
        for i in range(length-2, -1, -1):
            maxRem[i] = max(maxRem[i+1], string[i])
            
        # remove from string in a greedy manner
        i = 0
        while i < length:
            if string[i] == maxRem[i]:
                string.pop(i)
                maxRem.pop(i)
                length -= 1
            else:
                i += 1
        count += 1

    print("Case {}: {}".format(T, count))
    T += 1
    