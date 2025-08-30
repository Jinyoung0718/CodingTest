def solution(m, n, startX, startY, balls):
    answer = []

    def getDist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)

    for (ballX, ballY) in balls:
        # 위쪽 벽 대칭: (a, n + (n - b))
        distU = getDist(startX, startY, ballX, n + (n - ballY))
        
        # 아래쪽 벽 대칭: (a, -b)
        distD = getDist(startX, startY, ballX, -ballY)
        
        # 왼쪽 벽 대칭: (-a, b)
        distL = getDist(startX, startY, -ballX, ballY)
        
        # 오른쪽 벽 대칭: (m + (m - a), b)
        distR = getDist(startX, startY, m + (m - ballX), ballY)

        # 시작점과 목표 공이 일직선상일 때 불가능한 경로 제거
        if startX == ballX:
            if startY > ballY:
                distD = float('inf')
            else:
                distU = float('inf')

        if startY == ballY:
            if startX > ballX:
                distL = float('inf')
            else:
                distR = float('inf')

        dist = min((distU, distD, distL, distR))
        answer.append(dist)

    return answer
