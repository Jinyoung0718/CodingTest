computer = int(input())
pair = int(input())
tree = [[] for _ in range(computer + 1)]
visited = [False] * (computer + 1)

for _ in range(pair):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

def dfs(v, arr):
    visited[v] = True
    for next_v in tree[v]:
        if not visited[next_v]:
            arr.append(next_v)
            dfs(next_v, arr)
    return arr

answer = dfs(1, [])
print(len(answer))