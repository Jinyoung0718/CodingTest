import heapq
import sys

input = sys.stdin.readline

# 입력 처리
n = int(input())        # 도시 수
m = int(input())        # 버스 수

graph = {i: [] for i in range(1, n + 1)}  # 도시는 1번부터 n번까지

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # (비용, 도착 도시)

start, end = map(int, input().split())

def dijkstra(graph, start_v, dest_v):
    inf = sys.maxsize
    distances = [inf] * (len(graph) + 1)
    pq = []
    heapq.heappush(pq, (0, start_v))
    distances[start_v] = 0

    while pq:
        cur_d, cur_v = heapq.heappop(pq)
        if distances[cur_v] < cur_d:
            continue
        for next_cost, next_v in graph[cur_v]:
            next_d = cur_d + next_cost
            if next_d < distances[next_v]:
                heapq.heappush(pq, (next_d, next_v))
                distances[next_v] = next_d
    return distances[dest_v]

print(dijkstra(graph, start, end))
