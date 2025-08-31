def solution(board):
    # 1. O, X 개수 세기
    o_count = sum(row.count('O') for row in board)
    x_count = sum(row.count('X') for row in board)

    # 승리 여부 체크 함수
    def is_winner(ch):
        # 가로
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == ch:
                return True
        
        # 세로
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == ch:
                return True
        
        # 대각선
        if board[0][0] == board[1][1] == board[2][2] == ch:
            return True
        
        if board[0][2] == board[1][1] == board[2][0] == ch:
            return True
        
        return False

    o_win = is_winner('O')
    x_win = is_winner('X')

    # O가 선공이기에 되야만 하는 조건이 안 되면 0 반환
    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    # O가 이겼다면 O_count == X_count + 1
    if o_win and o_count != x_count + 1:
        return 0

    # X가 이겼다면 O_count == X_count
    if x_win and o_count != x_count:
        return 0

    # 둘 다 이기면 불가능
    if o_win and x_win:
        return 0

    return 1