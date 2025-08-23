from collections import deque

def all_bfs(graph, ch):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == ch:
                graph[i][j] = '.'

def out_side_bfs(graph, ch):
    n, m = len(graph), len(graph[0])
    padH, padW = n + 2, m + 2

    pad = [['.'] * padW for _ in range(padH)]
    for i in range(n):
        for j in range(m):
            pad[i+1][j+1] = graph[i][j]

    q = deque([(0, 0)])
    visited = [[False]*padW for _ in range(padH)]
    visited[0][0] = True

    to_remove = set()
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < padH and 0 <= nc < padW and not visited[nr][nc]:
                cell = pad[nr][nc]
                if cell == '.':
                    visited[nr][nc] = True
                    q.append((nr, nc))
                elif cell == ch:
                    gi, gj = nr-1, nc-1
                    if 0 <= gi < n and 0 <= gj < m and graph[gi][gj] == ch:
                        to_remove.add((gi, gj))

    # BFS가 끝난 뒤 한 번에 제거 (동시성 보장)
    for i, j in to_remove:
        graph[i][j] = '.'

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    graph = [list(row) for row in storage]

    for req in requests:
        ch = req[0]
        if len(req) == 1:
            out_side_bfs(graph, ch)   # 지게차
        else:
            all_bfs(graph, ch)        # 크레인

    return sum(1 for i in range(n) for j in range(m) if graph[i][j] != '.')
