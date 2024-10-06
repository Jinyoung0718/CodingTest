from collections import deque

def bfs():
    queue = deque()
    queue.append(0)
    visited[0] = 0
    while queue:
        cur_v = queue.popleft()
        if cur_v == n:
            print(visited[cur_v])
            quit()
        for next_v in (cur_v + 3, cur_v + 5):
            if visited[next_v] == 0 and next_v <= n:
                visited[next_v] =  visited[cur_v] + 1
                queue.append(next_v)
    print(-1)

n = int(input())
visited = [0] * (n + 5)
bfs()