# Competitive Programming 3
# Problem 12247

def guaranteedWin(hand1, hand2):
    h1 = sorted(hand1, reverse=True)
    h2 = sorted(hand2, reverse=True)
    
    if not (h2[0] > h1[1] and h2[1] > h1[2]):
        return True
    else: return False

while True:
    cards = [int(x) for x in input().split()]
    if sum(cards) == 0:
        break
    
    hand1, hand2 = cards[:3], cards[3:]
    extraCard = 1

    while extraCard in hand1 + hand2: extraCard += 1
    
    while not guaranteedWin(hand2 + [extraCard], hand1):
        extraCard += 1
        while extraCard in hand1 + hand2: extraCard += 1
        
        if extraCard > 52:
            break
        
    print(extraCard if extraCard <= 52 else -1)