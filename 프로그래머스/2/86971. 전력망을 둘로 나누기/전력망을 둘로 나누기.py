from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return count

def solution(n, wires):
    answer = n - 2

    for i in range(len(wires)):
        temp = wires[:i] + wires[i+1:] # i번째 전선을 끊는 역할
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)

        for x, y in temp:
            graph[x].append(y)
            graph[y].append(x)

        for node in range(1, n + 1):
            if graph[node]:
                start = node
                break

        a = bfs(graph, start, visited)
        b = n - a
        answer = min(answer, abs(a - b))

    return answer