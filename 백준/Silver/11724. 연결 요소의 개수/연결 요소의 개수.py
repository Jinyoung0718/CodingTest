import sys
input = sys.stdin.readline

from collections import deque


n, m = map(int, input().split())

graph = [[] * n for _ in range(n + 1)]  
# 정점 간의 연결을 나타내려면, 정점의 개수(n) 크기를 기준으로 그래프를 구성하는 것
visited = [False] * (n+1)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs(v):
    visited[v] = True
    queue = deque([v])
    while queue:
        cur_v = queue.popleft()
        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)


result = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)