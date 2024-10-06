import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] * n for _ in range(n)]
visited = [False] * n

for _ in range(m):
    s, e = map(int ,input().split())
    graph[s].append(e)
    graph[e].append(s)

result = False 

def dfs(v, depth):
    global result

    if depth == 5:
        result = True
        return

    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v, depth + 1)

    visited[v] = False
    
    return result

for i in range(n):
    dfs(i, 1)
    if result:
        break


if result:
    print(1)
else:
    print(0)