# Competitive Programming 3
# Problem p11254

while True:
    
    N = int(input())
    if N < 0: break
    
    # N = AP sum
    # n = number of terms
    # t = first term
    # then 2N = n^2 + (2t-1)n , so max n = sqrt(2N)
    for n in range(int((2*N)**0.5 + 0.5), 0, -1):
        
        if (2*N - n**2 + n) % 2*n == 0:
            t = (2*N - n**2 + n) // (2*n)
        else:
            continue
        
        if 2*N == n**2 + (2*t - 1)*n:
            break
    
    print("{} = {} + ... + {}".format(N, t, t+(n-1)))