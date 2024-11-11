n = int(input())
graph = [[0]*101 for _ in range(101)]
result = 0

# 0:(→), 1:(↑), 2:(←), 3:(↓)

dx = [0, -1, 0, 1]
dy = [1, 0, -1 ,0]

for _ in range(n):
    start_y,start_x,dir, g = map(int, input().split())
    temp = [(start_x, start_y)]                     
    temp.append((start_x + dx[dir], start_y + dy[dir]))

    for _ in range(g):           
        end_x,end_y = temp[-1]
        for i in range(len(temp)-2, -1, -1):
            cur_x, cur_y = temp[i]
            temp.append((end_x - (end_y - cur_y), end_y + (end_x - cur_x)))

    for x, y in temp:
        graph[x][y] = 1

for i in range(100):
    for j in range(100):
        if graph[i][j] == graph[i][j+1] == graph[i+1][j] == graph[i+1][j+1] ==1:
            result += 1

print(result)

# x가 증가하면 그만큼 y가 증가
# x가 감소하면 그만큼 y가 감소

# y가 증가하면 그만큼 x가 감소
# y가 감소하면 그만큼 x가 증가