n, k = map(int, input().split()) # n: 동전의 종류, k: 목표 값
arr = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1 # 0을 구할 수 있는 코인은 없지만 경우의 수이기 1 대입 필수

for coin in arr:
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]

print(dp[k])