def solution(my_string):
    answer = [0 for i in range(52)]
    
    for strig in my_string:
        if strig.isupper(): k = 65
        else: k = 71
        answer[ord(strig) - k] += 1
    return answer
        