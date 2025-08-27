def solution(num):
    answer = 0
    v1 = [False] * num          # 같은 열 체크
    v2 = [False] * (2 * num)    # 오른쪽 아래 대각선 (row+col)
    v3 = [False] * (2 * num)    # 왼쪽 아래 대각선 (row-col)

    def dfs(row):
        nonlocal answer
        if row == num:
            answer += 1
            return

        for col in range(num):
            if not v1[col] and not v2[row + col] and not v3[row - col]:
                v1[col] = v2[row + col] = v3[row - col] = True
                dfs(row + 1)
                v1[col] = v2[row + col] = v3[row - col] = False

    dfs(0)
    return answer
