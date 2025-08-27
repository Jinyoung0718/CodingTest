computer = int(input())
pair = int(input())
tree = [[] for _ in range(computer + 1)]
visited = set()

for _ in range(pair):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

def dfs(v, arr):
    visited.add(v)
    for next_v in tree[v]:
        if next_v not in visited:
            arr.append(next_v)
            dfs(next_v, arr)
            
    return arr

answer = dfs(1, [])
print(len(answer))