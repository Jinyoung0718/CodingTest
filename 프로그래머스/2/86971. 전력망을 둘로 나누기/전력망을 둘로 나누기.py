from collections import deque

def bfs(graph, visited, start_node):
    visited[start_node] = True
    queue = deque()
    queue.append((start_node))
    count = 1
    
    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                count += 1
    
    return count
            
        
def solution(n, wires):
    answer = n - 2
    
    for i in range(len(wires)):
        temp = wires[:i] + wires[i+1:]
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        
        for x, y in temp:
            graph[x].append(y)
            graph[y].append(x)
        
        for node in range(1, n + 1):
            if graph[node]:
                start = node
                break
        
        a = bfs(graph, visited, start)
        b = n - a
        answer = min(answer, abs(a - b))
    
    return answer
    
    