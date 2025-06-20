num = int(input())

dp = [[0] * 10 for _ in range(num + 1)]
dp[1] = [1] * 10

for i in range(2, num + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][j:])

answer = sum(dp[num])
print(answer % 10007)