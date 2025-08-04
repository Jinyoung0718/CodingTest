def solution(triangle):
    n = len(triangle)

    for i in range(n - 2, -1, -1):  # 아래에서 위로
        for j in range(len(triangle[i])):
            # 아래층의 두 자식 중 큰 값을 현재 값에 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]