# Competitive Programming 3
# Problem 10284

from itertools import product

def inRange(index):
    return True if (index >= 0 and index <= 7) else False

def updateThreats(board, threats):
    for i, j in product(range(8), repeat=2):
        
        # pawns
        if board[i][j] == 'p' and i != 7:
            threats[i+1][max(j-1,0)] = True
            threats[i+1][min(j+1,7)] = True
        
        elif board[i][j] == 'P' and i != 0:
            threats[i-1][max(j-1,0)] = True
            threats[i-1][min(j+1,7)] = True
            
        # kings
        if board[i][j] in ['k', 'K']:
            for x in range(max(0,i-1), min(8,i+2)):
                for y in range(max(0,j-1), min(8,j+2)):
                    threats[x][y] = True
                    
        # bishops + queens
        if board[i][j] in ['b', 'B', 'q', 'Q']:
            for dx, dy in product([-1,1], repeat=2):    # all four directions
                x, y = i, j
                while inRange(x+dx) and inRange(y+dy) and board[x+dx][y+dy] == '0':
                    threats[x+dx][y+dy] = True
                    x, y = x+dx, y+dy
                    
        # rooks + queens
        if board[i][j] in ['r', 'R', 'q', 'Q']:
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:    # all four directions
                x, y = i, j
                while inRange(x+dx) and inRange(y+dy) and board[x+dx][y+dy] == '0':
                    threats[x+dx][y+dy] = True
                    x, y = x+dx, y+dy
                    
        # knights
        if board[i][j] in ['n', 'N']:
            x, y = i, j
            for dx, dy in product([-1,1,-2,2], repeat=2): 
                if abs(dx) + abs(dy) != 3: continue # invalid combinations
                
                if inRange(x+dx) and inRange(y+dy):
                    threats[x+dx][y+dy] = True
        
    return threats
                
                

while True:
    try:
        FEN = [x for x in input().split('/')]
    except EOFError:
        break
    
    board = [['0' for x in range(8)] for y in range(8)]
    threats = [[False for x in range(8)] for y in range(8)]
    
    for r in range(8):
        skip = 0
        for c in range(len(FEN[r])):
            if FEN[r][c].isalpha():
                board[r][c+skip] = FEN[r][c]
                threats[r][c+skip] = True
            else:
                skip += int(FEN[r][c]) - 1
                
    threats = updateThreats(board, threats)
    print(sum(threats[i].count(False) for i in range(8)))
    
    
    