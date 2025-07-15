n, k = map(int, input().split())

coins = set(int(input()) for _ in range(n))

INF = k + 1
dp = [[INF] * (k + 1) for _ in range(len(coins) + 1)]

coins = list(coins)

for i in range(len(coins) + 1):
    dp[i][0] = 0

for i in range(1, len(coins) + 1):
    coin = coins[i - 1]
    for j in range(1, k + 1):
        if j >= coin:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - coin] + 1)
        else:
            dp[i][j] = dp[i - 1][j]

ans = dp[len(coins)][k]
print(-1 if ans == INF else ans)