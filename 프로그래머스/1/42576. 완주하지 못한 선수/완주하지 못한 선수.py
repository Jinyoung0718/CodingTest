def solution(participant, completion):
    memo = {}
    
    for person in participant:
        if person in memo:
            memo[person] += 1
            continue
        memo[person] = 1
    
    for person in completion:
        if person in memo:
            memo[person] -= 1
    
    answer = "".join([key for key, value in memo.items() if value != 0])
    return answer