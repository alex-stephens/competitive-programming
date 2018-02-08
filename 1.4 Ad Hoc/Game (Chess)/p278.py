# Competitive Programming 3
# Problem 278

T = int(input())

for _ in range(T):
    inputStr = input().split()
    piece, m, n = inputStr[0], int(inputStr[1]), int(inputStr[2])
    
    if piece == 'k':
        print( (m*n + 1) // 2 )
    
    elif piece == 'r' or piece == 'Q':
        print(min(m, n))
        
    elif piece == 'K':
        print( ((n+1)//2) * ((m+1)//2))