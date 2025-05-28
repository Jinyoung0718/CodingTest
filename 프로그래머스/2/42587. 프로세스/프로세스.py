from collections import deque

def solution(prior, location):
    queue = deque((i, p) for i, p in enumerate(prior))
    result = 0

    while queue:
        idx, val = queue.popleft()
        has_higher = False
        
        for _, p in queue:
            if p > val:
                has_higher = True
                break

        if has_higher:
            queue.append((idx, val))
        else:
            result += 1
            if idx == location:
                return result