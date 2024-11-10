from collections import deque

dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

n = int(input())
graph = [[0] * n for _ in range(n)]
result = 0

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

l = int(input())
distance = deque()

for _ in range(l):
    time, direct = input().split()
    distance.append((int(time), direct))

snake = deque()
snake.append((0, 0))
dir = 0

while True:
    cur_x, cur_y = snake[-1]
    next_x = cur_x + dx[dir]
    next_y = cur_y + dy[dir]
    result += 1

    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or (next_x, next_y) in snake:
        print(result)
        break

    if graph[next_x][next_y] == 1:
        graph[next_x][next_y] = 0
        snake.append((next_x, next_y))
    else:
        snake.append((next_x, next_y))
        snake.popleft()
    
    if distance and result == distance[0][0]:
        time, direct = distance.popleft()
        if direct == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4