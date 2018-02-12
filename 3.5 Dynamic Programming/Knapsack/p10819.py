# Competitive Programming 3
# Problem 10819

import math

while True:
    try:
        [M, N] = [int(x) for x in input().split()]
    except EOFError:
        break
    
    price, favour = [0 for _ in range(N+1)], [0 for _ in range(N+1)]
    M += 200 if M > 1800 else 0
    
    for i in range(1,N+1):
        price[i], favour[i] = [int(x) for x in input().split()]
        
    gcd = price[i]
    for i in range(1,N):
        gcd = math.gcd(price[i], gcd)
    if gcd > 1 and M % gcd == 0: 
        M //= gcd
        for i in range(N+1):
            price[i] //= gcd
                        
    #print('price = ', price)
    #print('favour = ', favour)
    #print('M = ', M, ', N = ', N)    
    
    F = [[0 for _ in range(M+1)] for _ in range(N+1)]
    spend = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    for n in range(1,N+1):
        for m in range(1,M+1):
            if price[n] > maxSpend:
                F[n][m] = F[n-1][m]
            else:
                # F[n][m] = max(F[n-1][m], favour[n] + F[n-1][m - price[n]])
                if F[n-1][m] > favour[n] + F[n-1][m - price[n]]:
                    F[n][m] = F[n-1][m]
                else:
                     F[n][m] = favour[n] + F[n-1][m - price[n]])
    
    print(F[-1][-1])