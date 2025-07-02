from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 1. 모든 사각형을 2배 확장해서 그래프에 표시
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                graph[i][j] = 1

    # 2. 내부를 0으로 덮어서 테두리만 남김
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
        for i in range(y1 + 1, y2):
            for j in range(x1 + 1, x2):
                graph[i][j] = 0

    # 3. 좌표도 2배 확장
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    def bfs(x, y):
        visited[y][x] = True
        queue = deque()
        queue.append((x, y, 0))
        while queue:
            cur_x, cur_y, cur_val = queue.popleft()
            if cur_x == itemX and cur_y == itemY:
                return cur_val // 2

            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if graph[next_y][next_x] == 1 and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    queue.append((next_x, next_y, cur_val + 1))

    return bfs(characterX, characterY)
