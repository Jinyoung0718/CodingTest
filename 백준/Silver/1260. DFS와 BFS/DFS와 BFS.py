from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v, arr1):
    arr1.append(v)
    visited_dfs[v] = True
    for next_v in sorted(graph[v]):
        if not visited_dfs[next_v]:
            dfs(next_v, arr1)

    return arr1

def bfs(v, arr2):
    arr2.append(v)
    visited_bfs[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        cur_v = queue.popleft()
        for next_v in sorted(graph[cur_v]):
            if not visited_bfs[next_v]:
                visited_bfs[next_v] = True
                arr2.append(next_v)
                queue.append(next_v)
    
    return arr2

visited_dfs = [False] * (n + 1)
print(" ".join(map(str, dfs(v, []))))

visited_bfs = [False] * (n + 1)
print(" ".join(map(str, bfs(v, []))))