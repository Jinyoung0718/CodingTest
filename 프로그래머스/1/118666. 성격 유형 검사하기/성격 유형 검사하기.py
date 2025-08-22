def solution(survey, choices):
    answer = ""
    
    pairs = [('R','T'), ('C','F'), ('J','M'), ('A','N')]
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for s, c in zip(survey, choices):
        disagree, agree = s[0], s[1]
        
        if c in [1, 2, 3]:  # 비동의 쪽
            score[disagree] += 4 - c
            
        if c in [5, 6, 7]:  # 동의 쪽
            score[agree] += c - 4
    
    for a, b in pairs:
        # 성격은 각 지표에서 두 유형 중 하나로 결정됩니다
        if score[a] > score[b]:
            answer += a
            
        elif score[a] < score[b]:
            answer += b
        
        else:
            answer += min(a, b)  # 동점이면 사전순 빠른 쪽 -> min으로 알파벳 사전순 추출 가능
    
    
    return answer