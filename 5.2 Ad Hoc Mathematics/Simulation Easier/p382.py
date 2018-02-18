# Competitive Programming 3
# Problem 382

''' 
prints PERFECT, ABUNDANT, or DEFICIENT
'''
def perfect(n):
    divsum = 0
    for i in range(1,int(n**0.5 + .05) + 1):
        if n % i == 0:
            divsum += i if n != 1 else 0
            if i > 1 and i**2 != n: 
                divsum += n//i

    if divsum == n: print("PERFECT")
    elif divsum < n: print("DEFICIENT")
    else: print("ABUNDANT")

done = False
print("PERFECTION OUTPUT")

while not done:
   
    numbers = [int(x) for x in input().split()]
    if numbers[-1] == 0:
        numbers.pop()
        done = True
    
    for n in numbers:
        print("{:5d}  ".format(n), end='')
        perfect(n)
        
print("END OF OUTPUT")
        