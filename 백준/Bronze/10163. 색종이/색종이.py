n = int(input())
arr = [[-1] * 1001 for _ in range(1001)]

for papter_id in range(n):
    x1, y1, width, height = map(int, input().split())

    for i in range(x1, x1 + width):
        for j in range(y1, y1 + height):
            arr[i][j] = papter_id
    
area = [0] * n

for i in range(1001):
    for j in range(1001):
        if arr[i][j] != -1:
            area[arr[i][j]] += 1

for i in area:
    print(i)