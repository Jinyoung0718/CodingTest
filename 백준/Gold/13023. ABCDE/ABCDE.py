import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

people, relation = map(int, input().split())
graph = [[] for _ in range(people)]
visited = [False] * people
result = False

for _ in range(relation):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v, depth):

    global result
    visited[v] = True

    if depth == 4:
        result = True
        return result

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v, depth + 1)
    
    visited[v] = False

for i in range(people):
    dfs(i, 0)
    if result:
        break

if result: print(1)
else: print(0)