n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

INF = k + 1
dp = [[INF] * (k + 1) for _ in range(n + 1)]
coins = list(set(coins))
n = len(coins) # coin의 중복제거로 n이 줄어듦을 고려

for i in range(n + 1):
    dp[i][0] = 0

for i in range(1, n + 1):
    coin = coins[i - 1]
    for j in range(1, k + 1):
        if j >= coin:
            dp[i][j] = min(
                dp[i - 1][j],
                dp[i][j - coin] + 1
            )
        else:
            dp[i][j] = dp[i - 1][j]

answer = dp[n][k]

if answer == INF:
    print(-1)
else:
    print(answer)