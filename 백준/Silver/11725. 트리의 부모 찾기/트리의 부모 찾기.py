from collections import deque

n = int(input())
tree = [[] for _ in range (n + 1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)


for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def levelorder(node):
    visited[node] = True
    queue = deque()
    queue.append(node)
    while queue:
        cur_node = queue.popleft()
        for next_node in tree[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                parent[next_node] = cur_node
                queue.append(next_node)

levelorder(1)

for i in range(2,n+1):
    print(parent[i])