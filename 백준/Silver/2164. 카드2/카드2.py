from collections import deque

N = int(input())
MyQueue = deque()

for i in range(1, N+1):
    MyQueue.append(i)

while len(MyQueue) > 1:
    MyQueue.popleft()
    MyQueue.append(MyQueue.popleft())

print(MyQueue[0])