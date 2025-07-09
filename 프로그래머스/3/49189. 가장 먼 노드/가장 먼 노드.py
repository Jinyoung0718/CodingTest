from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    visited = [False] * (n + 1)
    distance = [0] * (n + 1)

    def bfs(start_node):
        visited[start_node] = True
        queue = deque([(start_node, 0)])
        while queue:
            cur_node, cur_val = queue.popleft()
            distance[cur_node] = cur_val

            for next_node in graph[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append((next_node, cur_val + 1))

    bfs(1)
    max_dist = max(distance)
    
    return distance.count(max_dist)