from collections import deque

n = int(input())
queue = deque()
answer = []

for num in range(1, n + 1):
    queue.append(num)

process = 0

while len(queue) >= 1:
    process += 1
    num = queue.popleft()

    if process % 2 != 0:
        answer.append(num)
    else:
        queue.append(num)

print(*answer)