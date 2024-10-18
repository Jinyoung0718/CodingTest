from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
queue = deque()

for i in range(n):
    queue.insert(len(queue) - numbers[i], i + 1)

print(" ".join(map(str, queue)))