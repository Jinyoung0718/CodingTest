n = int(input())
arr = [0] + list(map(int, input().split()))

# dp[i][j] → i: i번 카드팩까지 고려했을 때, j개의 카드를 만들 수 있는 최대 비용
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):  # i: 현재 사용할 수 있는 카드팩 종류 (1~i번까지)
    for j in range(1, n + 1):  # j: 현재 목표 카드 개수 (상태값)
        if j - i >= 0:
            # i개짜리 카드팩을 사용할 수 있는 경우:
            # 사용 안 한 경우 vs 사용한 경우 중 최댓값 갱신
            dp[i][j] = max(dp[i - 1][j], dp[i][j - i] + arr[i])
        else:
            # i개짜리 카드팩을 사용할 수 없는 경우 → 이전 상태 유지
            dp[i][j] = dp[i - 1][j]

print(dp[n][n])