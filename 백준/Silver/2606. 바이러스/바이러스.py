from collections import deque

computer = int(input())
relation = int(input())

net = [[] for _ in range(computer + 1)]
visited = [False for _ in range(computer + 1)]
visited[0] = True


for _ in range(relation):
    s, e = map(int, input().split())
    net[s].append(e)
    net[e].append(s)

def bfs(v):
    visited[v] = True
    count = 0
    queue = deque()
    queue.append(v)
    while queue:
        cur = queue.popleft()
        for next_cur in net[cur]:
            if visited[next_cur] == False:
                visited[next_cur] = True
                queue.append(next_cur) 
                count += 1
    print(count)

bfs(1)