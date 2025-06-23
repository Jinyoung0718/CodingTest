import sys

input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())

# 거리 배열 초기화
dist = [[INF] * n for _ in range(n)]

# 자기 자신 → 자기 자신은 0
for i in range(n):
    dist[i][i] = 0

# 버스 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 도시 번호를 0-indexed로 조정
    dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c)  # 중복 경로 고려

# 플로이드 워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 결과 출력
for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
