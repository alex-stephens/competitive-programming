# Competitive Programming 3
# Problem 11413

def success(containers, m, capacity):

    currentAlloc = 0
    currentContainer = 1

    for i in range(len(containers)):
        if containers[i] > capacity:
            return False

        if currentAlloc + containers[i] <= capacity:
            currentAlloc += containers[i]

        else:
            currentContainer += 1
            if containers[i] > capacity:
                return False
            currentAlloc += containers[i]

    return True if currentContainer <= m else False


while True:

    try:
        n,m = map(int, input().split())
    except EOFError:
        break

    containers = list(map(int, input().split()))


    # binary search the answer
    i, j = 1, sum(containers)

    while i < j:
        mid = (i + j) // 2

        if success(containers, m, mid):
            j = mid

        else:
            i = mid + 1

    print(j if success(containers, m, j) else i)
