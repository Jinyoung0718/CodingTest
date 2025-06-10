import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0

for _ in range(m):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

def dfs(num):
    visited[num] = True
    for cur_num in tree[num]:
        if not visited[cur_num]:
            dfs(cur_num)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)