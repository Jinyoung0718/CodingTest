from collections import deque

n = int(input())
data = list(map(int, input().split()))
queue = deque()

for i in range(n):
    queue.insert(len(queue) - data[i], i + 1)

print(" ".join(map(str, queue)))