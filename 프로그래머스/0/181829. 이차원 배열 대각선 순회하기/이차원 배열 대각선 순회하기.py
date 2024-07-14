def solution(board, k):
    
    result = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                result += board[i][j]
    return result