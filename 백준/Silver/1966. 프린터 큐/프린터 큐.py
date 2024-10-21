from collections import deque

t = int(input())

for _ in range(t):
    total, target = map(int, input().split())
    queue = deque(enumerate(map(int, input().split())))
    count = 0

    while queue:
        max_important = max([doc[1] for doc in queue])
        current_data = queue.popleft()
        
        if current_data[1] == max_important:
            count += 1
            if current_data[0] == target:
                print(count)
                break
        else:
            queue.append(current_data)