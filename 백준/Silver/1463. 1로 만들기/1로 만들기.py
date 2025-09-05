from collections import deque

def bfs(n):
    queue = deque()  # (현재 숫자, 연산 횟수)
    queue.append((n, 0))
    visited = set()
    visited.add(n)

    while queue:
        cur_num, cur_val = queue.popleft()

        if cur_num == 1:
            return cur_val

        next_nums = []

        if cur_num % 3 == 0:
            next_nums.append(cur_num // 3)

        if cur_num % 2 == 0:
            next_nums.append(cur_num // 2)

        next_nums.append(cur_num - 1)

        for nx in next_nums:
            if nx not in visited:
                visited.add(nx)
                queue.append((nx, cur_val + 1))

n = int(input())
print(bfs(n))