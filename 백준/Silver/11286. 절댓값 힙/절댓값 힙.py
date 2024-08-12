import heapq
import sys
input = sys.stdin.readline

N = int(input())
myQueue = []

for _ in range(N):
    request = int(input())
    if request == 0:
        if not myQueue:
            sys.stdout.write('0\n')
        else:
            temp = heapq.heappop(myQueue)
            sys.stdout.write(f'{temp[1]}\n')
    else:
        heapq.heappush(myQueue, (abs(request), request))
