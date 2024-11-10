import sys
input = sys.stdin.readline

n = int(input())
m = n // 2
graph = [list(map(int, input().split())) for _ in range(n)]
result = 100 * n * m

def dfs(depth, alst, blst):
    global result
    
    if depth == n:
        if len(alst) == len(blst):
            asum = bsum = 0
            for i in range(m):
                for j in range(m):
                    asum += graph[alst[i]][alst[j]]
                    bsum += graph[blst[i]][blst[j]]
            
            result = min(result, abs(asum - bsum))
        return

    dfs(depth + 1, alst + [depth], blst)
    dfs(depth + 1, alst, blst + [depth])

dfs(0, [], [])
print(result)