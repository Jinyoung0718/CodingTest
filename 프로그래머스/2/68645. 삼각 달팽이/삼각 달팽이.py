def solution(n):
    answer = []
    tri = [[0] * (i + 1) for i in range(n)]
    num = 1
    x, y = -1, 0
    
    # 현재 이동 방향이 몇 번째 단계인지를 나타냄
    for i in range(n):
        # 안쪽 for문이 방향 하나를 ‘쭉’ 끝까지 처리
        # 한 방향으로 움직이는 칸 수가 매 턴마다 1씩 줄어듦
        for _ in range(i, n):
            
            if i % 3 == 0:          # 아래
                x += 1
            
            elif i % 3 == 1:        # 오른쪽
                y += 1
            
            elif i % 3 == 2:                   # 왼쪽 위
                x -= 1
                y -= 1
        
            tri[x][y] = num
            num += 1
    
    for row in tri:
        for num in row:
            answer.append(num)
    
    return answer