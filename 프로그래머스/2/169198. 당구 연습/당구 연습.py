def solution(m, n, startX, startY, balls):
    answer = []

    def getDist(x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    for (ballX, ballY) in balls:
        distU = getDist(startX, startY, ballX, ballY + (2 * (n - ballY)))
        distD = getDist(startX, startY, ballX, -ballY)
        distL = getDist(startX, startY, -ballX, ballY)
        distR = getDist(startX, startY, ballX + (2 * (m - ballX)), ballY)

        if startX == ballX:
            if startY > ballY:
                distD = int(1e9)
            else:
                distU = int(1e9)

        if startY == ballY:
            if startX > ballX:
                distL = int(1e9)
            else:
                distR = int(1e9)

        dist = min((distU, distD, distL, distR))
        answer.append(dist)

    return answer