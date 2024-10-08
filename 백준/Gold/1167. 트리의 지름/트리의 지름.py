from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n):
    Data = list(map(int, input().split()))
    currnet_node = Data[0]
    index = 1
    while True:
        connect_node = Data[index]
        if connect_node == - 1:
            break
        distance = Data[index + 1]
        tree[currnet_node].append((connect_node, distance))
        index += 2

def bfs(v):
    visited[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        cur_node = queue.popleft()
        for next_node, dist in tree[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                distance[next_node] = distance[cur_node] + dist 


visited = [False] * (n + 1)
distance = [0] * (n + 1)
bfs(1)

far_node = 1

for i in range(2, n + 1): # distance 인덱스를 통해 가장 먼 ㄴ드 찾기
    if distance[far_node] < distance[i]:
        far_node = i

visited = [False] * (n + 1)
distance = [0] * (n + 1)
bfs(far_node) # 가장 먼 노드는 끝쪽 노드이기에 최고 거리를 재면, 지름의 길이가 됨
print(max(distance))