# Competitive Programming 3
# Problem 12192

from bisect import bisect_left, bisect_right

printing = False

while True:

    N, M = map(int, input().split())
    if N == 0 and M == 0: break

    grid = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        grid[i] = list(map(int, input().split()))

    Q = int(input())

    for q in range(Q):
        L, U = map(int, input().split())

        topLeft = [0 for _ in range(N)]
        bottomRight = [0 for _ in range(N)]

        for r in range(N):
            c = bisect_left(grid[r], L)
            topLeft[r] = c

            # could produce negative indices
            c = bisect_right(grid[r], U) - 1
            bottomRight[r] = c

        maxSize = 0

        for i in range(N):
            for j in range(i, N):

                if topLeft[i] == M or bottomRight[j] == -1:
                    continue

                ans = min(bottomRight[j] - topLeft[i], j - i) + 1

                maxSize = max(maxSize, ans)

        print(maxSize)
    print('-')
