def solution(survey, choices):
    answer = ""
    
    pairs = [('R','T'), ('C','F'), ('J','M'), ('A','N')]
    score = { 'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0 }
    
    for s, c in zip(survey, choices):
        disagree, agree = s[0], s[1]
        if c < 4:  # 비동의 쪽
            score[disagree] += 4 - c
        elif c > 4:  # 동의 쪽
            score[agree] += c - 4
    
    for a, b in pairs:
        if score[a] > score[b]:
            answer += a
        elif score[a] < score[b]:
            answer += b
        else:
            answer += min(a, b)  # 동점이면 사전순 빠른 쪽
    
    return answer
