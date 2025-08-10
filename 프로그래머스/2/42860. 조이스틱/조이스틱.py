def solution(name):
    answer = 0 
    n = len(name)
    move = n - 1
    
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    for i in range(n):
        next_i = i + 1
        
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        move = min(move, i * 2 + (n - next_i), (n - next_i) * 2 + i)
    
    answer += move
    return answer