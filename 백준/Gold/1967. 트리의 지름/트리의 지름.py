import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, value = map(int, input().split())
    tree[parent].append((child, value))
    tree[child].append((parent, value))


def dfs(node):
    for next_node, dist in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            distance[next_node] = distance[node] + dist 
            dfs(next_node)

visited = [False] * (n + 1)
visited[1] = True
distance = [0] * (n + 1)
dfs(1)

far_node = distance.index(max(distance))

visited = [False] * (n + 1)
visited[far_node] = True
distance = [0] * (n + 1)
dfs(far_node)

print(max(distance))