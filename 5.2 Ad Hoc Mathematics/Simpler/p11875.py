# Competitive Programming 3
# Problem 11875 

T = int(input())
for t in range(1,T+1):
    members = [int(x) for x in input().split()]
    N = members.pop(0)
    members.sort()

    print("Case {}: {}".format(t, members[N//2]))