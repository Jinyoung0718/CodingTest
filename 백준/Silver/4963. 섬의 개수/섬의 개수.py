import sys
# 재귀 깊이 한계 재설정
sys.setrecursionlimit(10**6)

def dfs(x,y):
    # 행렬 범위를 벗어나면 종료
    if x < 0 or x >= row or y < 0 or y >= col:
        return False
    
    # 좌표가 0일 경우 종료
    if graph[x][y] == 0:
        return False
    
    # 8방향 검사
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    
    if graph[x][y] == 1:
        # 방문 처리
        graph[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True

while True:
    #열,행 입력 받기
    col,row = map(int,input().split())
    if (col,row) == (0,0): break
    
    # 그래프 생성
    graph = []
    for i in range(row):
        graph.append(list(map(int,input().split())))

    # 모든 행과 열에 대해 검사하며 count
    cnt = 0
    for i in range(row):
        for j in range(col):
            if dfs(i,j):
                cnt += 1
    print(cnt)