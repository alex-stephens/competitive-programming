# Competitive Programming 3
# Problem 462

def val(rank):
    if   rank == 'A': return 4
    elif rank == 'K': return 3 
    elif rank == 'Q': return 2
    elif rank == 'J': return 1
    else: return 0

while True:
    try:
        hand = [x for x in input().split()]
    except EOFError:
        break
    
    rank = [card[0] for card in hand]
    suit = [card[1] for card in hand]
    points = sum([val(x) for x in rank])
    
    SUITS = ['S', 'H', 'D', 'C']
    
    counts = [suit.count(s) for s in SUITS]

    # subtractions
    for i in range(len(rank)):
        # king suit
        if rank[i] == 'K':
            kingSuit = suit[i]
            if suit.count(kingSuit) == 1:
                points -= 1
        
        # queen suit
        if rank[i] == 'Q':
            queenSuit = suit[i]
            if suit.count(queenSuit) <= 2:
                points -= 1

        # jack suit
        if rank[i] == 'J':
            jackSuit = suit[i]
            if suit.count(jackSuit) <= 3:
                points -= 1
    
    # additions
    beforeExtra = points
    for s in SUITS:
        if suit.count(s) == 2: points += 1
        if suit.count(s) in [0,1]: points += 2
    
    # all stopped? 
    stopped = 0
    for i in range(4):
        rankSubset = [rank[x] for x in range(len(rank)) if suit[x] == SUITS[i]]
        size = len(rankSubset)
        
        if rankSubset.count('A') == 1:                 stopped += 1
        elif rankSubset.count('K') == 1 and size >= 2: stopped += 1
        elif rankSubset.count('Q') == 1 and size >= 3: stopped += 1
    
    # evaluate
    if points < 14:
        print('PASS')
        continue    
    
    elif stopped == 4 and beforeExtra >= 16:
        print('BID NO-TRUMP')
    
    else:
        print('BID ' + str(SUITS[counts.index(max(counts))]))