from collections import deque

n = int(input()) 
tree = [[] for _ in range(n+1)]  

for _ in range(n):
    data = list(map(int, input().split()))  
    current_node = data[0]  
    idx = 1
    while True:
        contect_node = data[idx] 
        if contect_node == -1: 
            break
        distance = data[idx+1]  
        tree[current_node].append((contect_node, distance)) 
        idx += 2  

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True
    while queue:
        current_node = queue.popleft()
        for next_node, dist in tree[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                distance[next_node] = distance[current_node] + dist

distance = [0] * (n + 1)
visited = [False] * (n + 1)
bfs(1)

farthest_node = 1
for i in range(2, n+1):
    if distance[farthest_node] < distance[i]:
        farthest_node = i

distance = [0] * (n + 1)
visited = [False] * (n + 1)
bfs(farthest_node)
print(max(distance))