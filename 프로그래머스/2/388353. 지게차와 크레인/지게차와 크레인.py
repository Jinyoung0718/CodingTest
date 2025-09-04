from collections import deque

def solution(storage, requests):
    
    def all_side_bfs(graph, target):
        for i in range(1, len(graph) - 1):
            for j in range(1, len(graph[0]) - 1):
                if graph[i][j] == target:
                    graph[i][j] = '.'

    def out_side_bfs(graph, target):
        n, m = len(graph), len(graph[0])
        queue = deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0, 0))
        removed_set = set()
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if graph[nx][ny] == '.':
                        queue.append((nx, ny))
                    elif graph[nx][ny] == target:
                        removed_set.add((nx, ny))
        
        for i, j in removed_set:
            graph[i][j] = '.'
            

    answer = 0
    rows, cols = len(storage), len(storage[0])
    graph = [['.'] * (cols + 2)]
    
    for row in storage:
        graph.append(['.'] + list(row) + ['.'])
    
    graph.append(['.'] * (cols + 2))

    for req in requests:
        target = req[0]
        if len(req) == 2:
            all_side_bfs(graph, target)
        else:
            out_side_bfs(graph, target)
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if graph[i][j] != '.':
                answer += 1
    
    return answer