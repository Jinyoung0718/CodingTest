import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

people, relation = map(int, input().split())
graph = [[] * people for _ in range(people)]
visited = [False] * (people)

result = False

for _ in range(relation):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v, depth):
    global result

    if depth == 4:
        result = True
        return

    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v, depth + 1)
    
    visited[v] = False
    return result



for i in range(people):
    dfs(i, 0)
    if result:
        break

if result:
    print(1)
else:
    print(0)