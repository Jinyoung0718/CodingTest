def solution(n, con):
    dict = {'w':1, 's':-1, 'd':10, 'a':-10}
    result = n
    
    for i in range(0, len(con)):
        result += dict[con[i]]
    
    return result
        