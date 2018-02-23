# Competitive Programming 3
# Problem 495

while True:
    try:
        N = int(input())
    except EOFError:
        break
    
    fib = [0, 1, 1]
    
    for n in range(2,N+1):
        fib[n%3] = fib[(n-1)%3] + fib[(n-2)%3]
    
    print("The Fibonacci number for {} is {}".format(N, fib[N%3]))
