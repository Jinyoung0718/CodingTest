def solution(record):
    
    memo = {}
    answer = []
    
    for word in record:
        parts = word.split()
        
        if parts[0] == "Enter" or parts[0] == "Change":
            user_id = parts[1]
            nickname = parts[2]
            memo[user_id] = nickname
    
    
    for word in record:
        parts = word.split()
        user_id = parts[1]
        
        if parts[0] == "Enter":
            answer.append(f"{memo[user_id]}님이 들어왔습니다.")
        
        elif parts[0] == "Leave":
            answer.append(f"{memo[user_id]}님이 나갔습니다.")
    
    return answer