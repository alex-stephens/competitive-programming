# Competitive Programming 3
# Problem 11727

T = int(input())

for i in range(1,T+1):
    salaries = sorted([int(x) for x in input().split()])
    print('Case ' + str(i) + ': ' + str(salaries[1]))