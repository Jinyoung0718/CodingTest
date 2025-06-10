import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (m + 1) for _ in range(n + 1)]
D = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    A[i] = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(1, m+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

k = int(input())

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    answer = D[x2][y2] - D[x1-1][y2] -D[x2][y1-1] + D[x1-1][y1-1]
    print(answer)