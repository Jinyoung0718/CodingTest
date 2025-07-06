from collections import deque

def normalize(block):
    min_x = min(x for x, y in block)
    min_y = min(y for x, y in block)
    return sorted([(x - min_x, y - min_y) for x, y in block])

def bfs(start, board, visited, target):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    block = []
    n = len(board)

    while queue:
        x, y = queue.popleft()
        block.append((x, y))
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return normalize(block)

def rotate(block):
    return normalize([(-y, x) for x, y in block])

def find_blocks(board, target):
    n = len(board)
    visited = [[False]*n for _ in range(n)]
    blocks = []
        
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == target:
                blocks.append(bfs((i, j), board, visited, target))
                    
    return blocks

def solution(game_board, table):
    n = len(game_board)
    empty_spaces = find_blocks(game_board, 0)
    puzzle_pieces = find_blocks(table, 1)

    used = [False] * len(puzzle_pieces)
    answer = 0

    for space in empty_spaces:
        for i, piece in enumerate(puzzle_pieces):
            if used[i]:
                continue

            curr_piece = piece[:]
            for _ in range(4):
                if space == curr_piece:
                    answer += len(space)
                    used[i] = True
                    break
                curr_piece = rotate(curr_piece)
            if used[i]:
                break

    return answer

