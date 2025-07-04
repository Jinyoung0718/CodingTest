from collections import deque

student, count = map(int, input().split())

graph = [[] for _ in range (student + 1)]
in_degree = [0] * (student + 1)
queue = deque()
answer = []

for _ in range(count):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1 # B로의 진입차수

for i in range(1, student + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    cur_node = queue.popleft()
    answer.append(cur_node)

    for next_node in graph[cur_node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

print(*answer)