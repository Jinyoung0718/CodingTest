n = int(input())
INF = float('inf')

dp = [INF] * (n + 1)
dp[0] = 0

# 숫자 n의 제곱근의 범위를 아는 공식 -> int(n ** 0.5)
# i, 즉 열은 제곱근의 범위로 설정
for i in range(1, int(n ** 0.5) + 1):
    sq = i * i
    for j in range(sq, n + 1):
        dp[j] = min(dp[j], dp[j - sq] + 1)

print(dp[n])