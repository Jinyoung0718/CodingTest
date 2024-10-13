import sys
input = sys.stdin.readline

from collections import deque

n ,m = map(int ,input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    s, e = map(int ,input().split())
    graph[s].append(e)
    graph[e].append(s)


def bfs(cur_v):
    visited[cur_v] = True 
    queue = deque()
    queue.append(cur_v)
    while queue:
        cur_v = queue.popleft()
        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v) 

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)