n = int(input())
arr = [[False] * 101 for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = True

total = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(101):
    for j in range(101):
        if arr[i][j] == True:
            for k in range(4):
                next_i, next_y = i + dx[k], j + dy[k]
                if next_i < 0 or next_i >= 101 or next_y < 0 or next_y >= 101 or arr[next_i][next_y] == False:
                    total += 1
print(total)