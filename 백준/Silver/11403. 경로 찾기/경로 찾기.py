N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 플로이드–워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# 결과 출력
for row in graph:
    print(' '.join(map(str, row)))
