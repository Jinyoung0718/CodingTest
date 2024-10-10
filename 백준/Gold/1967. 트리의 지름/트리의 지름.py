import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

node_su = int(input())
tree = [[] for _ in range(node_su + 1)]

for _ in range(node_su - 1):
    parent, child, value = map(int, input().split())
    tree[parent].append((child, value))
    tree[child].append((parent, value))

def dfs(node, visited, distance):
    visited[node] = True
    for next_node, dist in tree[node]:
        if not visited[next_node]:
            distance[next_node] = distance[node] + dist
            dfs(next_node, visited, distance)
    
    return distance

visited = [False] * (node_su + 1)
distance = [0] * (node_su + 1)
distance_first = dfs(1, visited, distance)

far_node = distance_first.index(max(distance_first))
visited = [False] * (node_su + 1)
distance = [0] * (node_su + 1)

distance_result = dfs(far_node, visited, distance)

print(max(distance_result))