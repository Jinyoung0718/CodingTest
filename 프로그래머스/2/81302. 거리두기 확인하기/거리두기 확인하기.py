from collections import deque

def solution(places):
    answer = []
    
    def bfs(sx, sy, graph):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        queue = deque()
        queue.append((sx, sy, 0))
        
        visited = set()
        visited.add((sx, sy))
        
        while queue:
            x, y, dist = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                next_dist = dist + 1
                
                if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visited and next_dist <= 2:
                    visited.add((nx, ny))
                    
                    if graph[nx][ny] == 'P':
                        return False
                    
                    if graph[nx][ny] == 'O':
                        queue.append((nx, ny, next_dist))
        
        return True
    
    for graph in places:
        valid = True
        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    if not bfs(i, j, graph):
                        answer.append(0)
                        valid = False
                        break
                        
            if not valid:
                break
                
        if valid:
            answer.append(1)
    
    return answer            