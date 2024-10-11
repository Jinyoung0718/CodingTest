from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()
result = 0

for _ in range(n):
    queue.put(int(input()))

while queue.qsize() > 1:
    data1 = queue.get()
    data2 = queue.get()
    temp = data1 + data2
    result += temp
    queue.put(temp)
    
print(result)