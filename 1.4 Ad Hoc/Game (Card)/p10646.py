# Competitive Programming 3
# Problem 10646

def val(card):
    rank = card[0]
    if   rank.isalpha() : return 10
    else:                 return int(rank) 

T = int(input())

for case in range(1,T+1):
    cards = []
    cards += [x for x in input().split()]

    Y = 0
    pile = list(cards[:-25])
    inHand = list(cards[-25:])

    for _ in range(3):
        X = val(pile[-1])
        Y += X
        pile[-(11-X):] = []
    
    pile += inHand
    finalCard = pile[Y-1]
    
    print('Case ' + str(case) + ': ' + str(finalCard))
    
