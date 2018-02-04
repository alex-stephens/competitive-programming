# Competitive Programming 3
# Problem 11799

T = int(input())

for i in range(1, T+1):
    speeds = [int(x) for x in input().split()]    
    print('Case ' + str(i) + ': ' + str(max(speeds)))
    