from collections import deque

testcase = int(input())
dx = [-2, -1, 1, 2, 2, 1, -2, -1]
dy = [-1, -2, -2, -1, 1, 2, 1, 2]

def bfs(x, y):
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    while queue:
        cur_x, cur_y, dist = queue.popleft()

        if cur_x == target_x and cur_y == target_y:
            return dist

        for i in range(8):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, dist + 1))

for _ in range(testcase):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    start, end = map(int, input().split())
    target_x, target_y = map(int, input().split())

    answer = bfs(start, end)
    print(answer)