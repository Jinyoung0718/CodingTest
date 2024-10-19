n = int(input())
arr = [[0] * 101 for _ in range(101)]
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            for k in range(4):
                next_i = i + dx[k]
                next_y = j + dy[k]
                if arr[next_i][next_y] == 0:
                    result += 1

print(result)