# Competitive Programming 3
# Problem 11517

from math import exp, sin, cos, tan

def f(line, x):
    p, q, r, s, t, u = line
    return p * exp(-x) + q*sin(x) + r*cos(x) + s*tan(x) + t*(x**2) + u

while True:

    try:
        line = list(map(int, input().split()))
    except EOFError:
        break

    if (f(line,0) > 0 and f(line,1) > 0) or (f(line,0) < 0 and f(line,1) < 0):
        print('No solution')
        continue

    grad = 1 if f(line,1) > f(line,0) else -1
    x = 0.5
    inc  = 0.25

    err = 1

    while err > 10**(-6):

        if f(line,x) > 0:
            x -= grad*inc
        elif f(line,x) < 0:
            x += grad*inc

        inc /= 2

        err = abs(f(line,x))

    print('{:.4f}'.format(x))
