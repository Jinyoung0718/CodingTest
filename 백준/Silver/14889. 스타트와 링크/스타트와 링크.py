import sys
input = sys.stdin.readline

def dfs(count, alst, blst):
    global result

    if count == n:
        if len(alst) == len(blst):
            asm = bsm = 0
            for i in range(m):
                for j in range(m):
                    asm += graph[alst[i]][alst[j]]
                    bsm += graph[blst[i]][blst[j]]
            result = min(result, abs(asm - bsm))
        return

    dfs(count + 1, alst + [count], blst)
    dfs(count + 1, alst, blst + [count])

n = int(input())
m = n//2
graph = [list(map(int, input().split())) for _ in range(n)]
result = 100 * m * n

dfs(0, [], [])
print(result)