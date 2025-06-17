row, col = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(row)]

answer = 1  # 최소 넓이는 1 (1x1 정사각형)

for i in range(row):
    for j in range(col):
        for k in range(1, min(row, col)):
            ni = i + k
            nj = j + k
            if ni < row and nj < col:
                if graph[i][j] == graph[i][nj] == graph[ni][j] == graph[ni][nj]:
                    answer = max(answer, (k+1) ** 2)

print(answer)