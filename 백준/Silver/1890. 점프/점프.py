N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for row in range(N):
    for col in range(N):
        if dp[row][col] == 0 or board[row][col] == 0:
            continue

        step = board[row][col]

        next_row = row + step
        next_col = col + step

        if next_row < N:
            dp[next_row][col] += dp[row][col]

        if next_col < N:
            dp[row][next_col] += dp[row][col]

print(dp[N - 1][N - 1])
