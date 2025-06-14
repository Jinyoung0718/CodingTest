n = int(input())
graph = [list(input()) for _ in range(n)]

dx = [0, 1]
dy = [1, 0]

def check(graph):
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(1, n):
            if graph[i][j] == graph[i][j-1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

    for i in range(n):
        count = 1
        for j in range(1, n):
            if graph[j][i] == graph[j-1][i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

    return max_count

answer = 0

for i in range(n):
    for j in range(n):
        for k in range(2):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < n and 0 <= nj < n and graph[i][j] != graph[ni][nj]:
                graph[i][j], graph[ni][nj] = graph[ni][nj], graph[i][j]
                answer = max(answer, check(graph))
                graph[i][j], graph[ni][nj] = graph[ni][nj], graph[i][j]

print(answer)