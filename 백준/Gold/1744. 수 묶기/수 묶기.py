from queue import PriorityQueue

n = int(input())
plusQueue = PriorityQueue()
minusQueue = PriorityQueue()

sum = 0
one = 0
zero = 0

for i in range(n):
    data = int(input())
    if data > 1:
        plusQueue.put(data * -1)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    elif data < 0:
        minusQueue.put(data)

while plusQueue.qsize() > 1: # 양수처리
    first = plusQueue.get() * -1
    second = plusQueue.get() * -1
    sum += first * second

if plusQueue.qsize() > 0:
    sum += plusQueue.get() * -1

while minusQueue.qsize() > 1: # 음수처리
    first = minusQueue.get() 
    second = minusQueue.get() 
    sum += first * second

if minusQueue.qsize() > 0:
    last_negative = minusQueue.get()
    if zero > 0:
        sum += last_negative * 0
    else:
        sum += last_negative

sum += one
print(sum)