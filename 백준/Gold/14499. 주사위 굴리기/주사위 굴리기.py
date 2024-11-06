import sys
input = sys.stdin.readline

def roll_dice(dir):
    if dir == 1:  # 동쪽
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif dir == 2:  # 서쪽
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif dir == 3:  # 북쪽
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif dir == 4:  # 남쪽
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dice = [0] * 6  

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for command in commands:
    nx = x + dx[command - 1]
    ny = y + dy[command - 1]

    if not (0 <= nx < n and 0 <= ny < m):
        continue

    roll_dice(command)

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]  
    else:
        dice[5] = graph[nx][ny]  
        graph[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])