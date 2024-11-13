def cal(tlst):
    sm = 0
    for hi,hj in home:
        mn = 2*N
        for ci,cj in tlst:
            mn = min(mn, abs(hi-ci)+abs(hj-cj))
        sm += mn
    return sm

def dfs(n, tlst):
    global ans
    
    if n==CNT:
        if len(tlst)==M:
            ans = min(ans, cal(tlst))
        return

    dfs(n+1, tlst+[chicken[n]])
    dfs(n+1, tlst)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            home.append((i,j))
        elif arr[i][j]==2:
            chicken.append((i,j))
CNT = len(chicken)

ans = 2*N*2*N
dfs(0, [])
print(ans)