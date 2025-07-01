N, K = map(int, input().split())
wv = [(0, 0)]

for i in range(1, N + 1):
    w, v = map(int, input().split())
    wv.append((w,v))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = wv[i]
    for k in range(1, K + 1):
        if k >= w:
            dp[i][k] = max(
                dp[i - 1][k],
                dp[i - 1][k - w] + v
            )
        else:
            dp[i][k] = max(dp[i-1][k], dp[i][k-1])

print(dp[N][K])