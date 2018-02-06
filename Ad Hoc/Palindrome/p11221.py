# Competitive Programming 3
# Problem 11221

def isPalindrome(string):
    return True if string == string[::-1] else False

def alphaOnly(string):
    result = ''
    for i in range(len(string)):
        if string[i].isalpha():
            result += string[i]
    return result

T = int(input())

for i in range(1, T+1):
    print('Case #' + str(i) + ':')
    
    string = alphaOnly(input())
    if not isPalindrome(string): 
        print('No magic :(')
        continue
    
    size = int(len(string) ** (1/2))
    if size ** 2 != len(string):
        print('No magic :(')
        continue
    
    matrix = [['0' for _ in range(size)] for _ in range(size)]
    pos = 0
    for i in range(size):
        for j in range(size):
            matrix[i][j] = string[pos]
            pos += 1
          
    magic = True
    for i in range(size):
        for j in range(i+1):
            if matrix[i][j] != matrix[j][i]:
                magic = False
                break
    
    if magic:
        print(size)
    else:
        print('No magic :(')
    
    
    
    
    