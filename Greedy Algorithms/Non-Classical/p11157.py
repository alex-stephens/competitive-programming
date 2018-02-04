# Competitive Programming 3
# Problem 11157

# Technique - use every second small rock on each trip

T = int(input())

for x in range(1,T+1):
    
    N, D = [int(x) for x in input().split()]
    
    stones = input().split()
    big, small1, small2 = [], [], []
    switch = True
    for i in range(len(stones)):
        if stones[i][0] == 'B':
            big.append(int(stones[i][2:]))
        else:
            if switch:
                small1.append(int(stones[i][2:]))
            else:
                small2.append(int(stones[i][2:]))
            switch = not switch

    maxJump, pos, prev = 0, 0, 0
    trip1 = [0] + sorted(big + small1) + [D]
    trip2 = [0] + sorted(big + small2) + [D]

    maxJump1 = max([trip1[i] - trip1[i-1] for i in range(1,len(trip1))])
    maxJump2 = max([trip2[i] - trip2[i-1] for i in range(1,len(trip2))])

    print('Case ' + str(x) + ': ' + str(max(maxJump1, maxJump2)))  
