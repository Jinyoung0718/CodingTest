import sys
sys.setrecursionlimit(10**9)

def dfs(cur_x, cur_y):
    if dp[cur_x][cur_y] == -1:
        dp[cur_x][cur_y]=0
        for i in range(4):
            prev_x = cur_x + dx[i]
            prev_y = cur_y + dy[i]
            if arr[prev_x][prev_y] > arr[cur_x][cur_y]: # 더 높은 곳으로 감 (역방향 추적)
                dp[cur_x][cur_y] += dfs(prev_x, prev_y)

    return dp[cur_x][cur_y]

N, M = map(int, input().split())
arr = [[0] * (M + 2)]+[[0] + list(map(int, input().split())) + [0] for _ in range(N)]+[[0] * (M + 2)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dp = [[-1] * (M + 2) for _ in range(N + 2)]
dp[1][1] = 1
print(dfs(N,M))