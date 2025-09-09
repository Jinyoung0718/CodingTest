from collections import deque

def solution(places):
    answer = []
    
    # BFS로 특정 위치에서 거리 2 이하 검사
    def bfs(x, y, graph):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        queue = deque()
        queue.append((x, y, 0))  # 시작 좌표와 거리 0
        
        while queue:
            cur_x, cur_y, dist = queue.popleft()
            
            # 시작점 제외, 다른 P 발견하면 위반
            if (cur_x, cur_y) != (x, y) and graph[cur_x][cur_y] == 'P':
                return False
            
            # 거리 2까지만 탐색
            # cur_x, cur_y는 더 이상 확장하지 않음
            # 큐에 남아 있는 다른 노드들만 계속 탐색
            if dist == 2:
                continue
            
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if graph[nx][ny] != 'X':  # 파티션이 아니면 이동 가능
                        queue.append((nx, ny, dist + 1))
        
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
            answer.append(1)  # 문제 없음
    
    return answer      
            