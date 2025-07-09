v, e = map(int, input().split())

union_list = [i for i in range(v + 1)]
edges = []
answer = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

def find(node):
    while union_list[node] != node:
        union_list[node] = union_list[union_list[node]]
        node = union_list[node]

    return node

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a != parent_b:
        union_list[parent_a] = parent_b
        return True
    return False

for cost, a, b in edges:
    if union(a, b):
        answer += cost

print(answer)
