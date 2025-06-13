import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = [0] * (n + 1)

for _ in range(n - 1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

def dfs(num):
    visited[num] = True
    for next_num in tree[num]:
        if not visited[next_num]:
            answer[next_num] = num
            dfs(next_num)

dfs(1)

print("\n".join(map(str, answer[2:])))
