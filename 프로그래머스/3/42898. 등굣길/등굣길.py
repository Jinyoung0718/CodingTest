def solution(m, n, puddles):
    
    MOD = 1000000007
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    puddles = set((y, x) for x, y in puddles)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) in puddles or (i == 1 and j == 1):
                continue
                
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[n][m]