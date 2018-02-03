# Competitive Programming 3
# Problem 10718

# Seems to work but gets Wrong Answer

def mask(a,b):
    binstr1, binstr2 = '{:032b}'.format(a), '{:032b}'.format(b)
    ans = ''
    for i in range(len(binstr1)):
        ans += max(binstr1[i], binstr2[i])
    return int(ans, 2)
    

while True:
    try:
        N, L, U = [int(x) for x in input().split()]
    except EOFError:
        break
    
    if N == 0:
        break
    
    # start with the largest bit
    bitval = 1
    while bitval * 2 <= U:
        bitval *= 2
    M = 0
    
    while bitval > 0:
        if M + (bitval - 1) < L:    # must add
            M += bitval
        elif mask(bitval, N) != N and M + bitval <= U:  # should add
            M += bitval
        bitval //= 2
    
    print(M)
