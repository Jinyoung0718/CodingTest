from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()

for _ in range(n):
    date = int(input())
    queue.put(date)

date1 = 0
date2 = 0
sum = 0

while queue.qsize() > 1:
    date1 = queue.get()
    date2 = queue.get()
    temp = date1 + date2
    sum += temp
    queue.put(temp)

print(sum)