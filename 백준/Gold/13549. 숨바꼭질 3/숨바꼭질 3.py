from collections import deque

n, k = map(int, input().split())
MAX_LIMIT = 10**6
visited = set()

def bfs(num):
    visited.add(num)
    queue = deque()
    queue.append((num, 0))
    while queue:
        cur_num, cur_val = queue.popleft()

        if cur_num == k:
            return cur_val

        for next_num in (cur_num  - 1, cur_num + 1, cur_num * 2):
            if 0 <= next_num <= MAX_LIMIT and next_num not in visited:
                visited.add(next_num)
                if next_num == cur_num * 2:
                    queue.appendleft((next_num, cur_val))
                else:
                    queue.append((next_num, cur_val + 1))

print(bfs(n))