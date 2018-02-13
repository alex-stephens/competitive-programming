# Competitive Programming 3
# Problem 11236

target = 2000

# only search for solutions a >= b >= c >= d to avoid duplication

for a in range(1,target-2): 
    for b in range(1,min(target-a-1, a+1)):
        for c in range(1,min(target-a-b-1, b+1)):
            
            if a*b*c <= 100**3:
                continue
            if (100**3 * (a+b+c)) % (a*b*c - 100**3) == 0 :
                
                d = (100**3 * (a+b+c)) // (a*b*c - 100**3)
            
            if d > c or a+b+c+d > 2000: continue
            
            if a * b * c * d == 100**3 * (a + b + c + d):
                print("{0:.2f} ".format(d/100), end='')
                print("{0:.2f} ".format(c/100), end='')
                print("{0:.2f} ".format(b/100), end='')
                print("{0:.2f}".format(a/100))