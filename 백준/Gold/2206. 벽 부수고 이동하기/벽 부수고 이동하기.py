from collections import deque

n, m = map(int, input().split())
graph = [[0] * (m + 2) for _ in range(n + 2)]
visited = [[[False] * 2 for _ in range(m + 2)] for _ in range(n + 2)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(1, n + 1):
    row = list(map(int, input()))
    for j in range(1, m + 1):
        graph[i][j] = row[j - 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y, 1, 1))  # (x, y, 거리, chance)
    visited[x][y][1] = True  # 벽 안 부순 상태로 시작

    while queue:
        cur_x, cur_y, cur_val, chance = queue.popleft()

        if cur_x == n and cur_y == m:
            return cur_val

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 1 <= next_x <= n and 1 <= next_y <= m:
                # 벽이 있지 않아도, 도달 시 해당 경로가 이전에 벽을 부셨거나 아니면 아니거나 둘 중 하나인 상황
                # 즉, 상태를 정확히 모르기에 chance 변수 그대로 사용
                if graph[next_x][next_y] == 0 and not visited[next_x][next_y][chance]:
                    visited[next_x][next_y][chance] = True
                    queue.append((next_x, next_y, cur_val + 1, chance))

                # 벽이 있고, 벽을 부술 찬스가 한 번 있고, 벽을 부수고 도착한 적이 없다.
                elif graph[next_x][next_y] == 1 and chance == 1 and not visited[next_x][next_y][0]:
                    visited[next_x][next_y][0] = True
                    queue.append((next_x, next_y, cur_val + 1, 0))

    return -1


print(bfs(1, 1))