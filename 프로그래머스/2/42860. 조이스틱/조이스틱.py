def solution(name):
    answer = 0
    n = len(name)
    
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    move = n - 1
    
    for i in range(n): # “턴 지점 후보” 를 전부 시도하는 루프
        next_i = i + 1
        
        # 그 후보(i)에 대해 “i 다음에 A가 얼마나 길게 이어지나?” 측정
        while next_i < n and name[next_i] == 'A':
            next_i += 1

        move = min(move, i * 2 + (n - next_i), (n - next_i) * 2 + i)
    
    
    
    answer += move    
    return answer