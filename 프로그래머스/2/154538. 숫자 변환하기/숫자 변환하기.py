from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))  # (현재값, 연산 횟수)
    visited = set([x])
    
    while queue:
        cur, cnt = queue.popleft()
        
        if cur == y:
            return cnt
        
        for nxt in (cur + n, cur * 2, cur * 3):
            if nxt <= y and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))
    
    return -1
