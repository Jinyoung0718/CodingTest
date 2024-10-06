from collections import deque

# 입력 받기
m, n = map(int, input().split())  # m: 가로(열), n: 세로(행)
graph = [list(map(int, input().split())) for _ in range(n)]  # 토마토 농장 상태 입력

# 상하좌우 이동을 위한 배열
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()

# 익은 토마토를 큐에 모두 넣음
for i in range(n):  # 행
    for j in range(m):  # 열
        if graph[i][j] == 1:
            queue.append((i, j))

# BFS 함수 정의
def bfs():
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            # 범위 내에 있고, 익지 않은 토마토(0)일 때
            if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == 0:
                graph[next_x][next_y] = graph[cur_x][cur_y] + 1  # 일수 증가
                queue.append((next_x, next_y))

bfs()

# 토마토가 모두 익는 데 걸리는 일수 계산
max_days = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:  # 익지 않은 토마토가 남아 있으면
            print(-1)
            exit()  # -1 출력 후 프로그램 종료
        max_days = max(max_days, graph[i][j])

# 처음 익은 토마토의 값이 1이므로 일수는 max_days에서 1을 뺀다
print(max_days - 1)
