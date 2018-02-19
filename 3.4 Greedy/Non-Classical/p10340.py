# Competitive Programming 3
# Problem 10340

while True:
    
    try:
        string, sub = input().split()
    except EOFError:
        break
    
    j = 0
    for i in range(len(sub)):
        if sub[i] == string[j]:
            j += 1
        if j >= len(string):
            break
    
    if j >= len(string):
        print('Yes')
    else:
        print('No')