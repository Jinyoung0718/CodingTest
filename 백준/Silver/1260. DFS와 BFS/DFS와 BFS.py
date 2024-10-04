from collections import deque


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v, visited, visited_set):
    visited.append(v)
    visited_set.add(v)
    for next_v in sorted(graph[v]):
        if next_v not in visited_set:
            dfs(next_v, visited, visited_set)
    
    return visited

def bfs(v, visited, visited_set):
    visited.append(v)
    visited_set.add(v)
    queue = deque()
    queue.append(v)
    while queue:
        cur_v = queue.popleft()
        for next_v in sorted(graph[cur_v]):
            if next_v not in visited_set:
                visited.append(next_v)
                visited_set.add(next_v)
                queue.append(next_v)

    return visited

print(" ".join(map(str, dfs(v, [], set()))))
print(" ".join(map(str, bfs(v, [], set()))))