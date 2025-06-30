def solution(records):
    answer = []
    memo = {}

    for record in records:
        parts = record.split()
        command = parts[0]
        user_id = parts[1]

        if command == 'Enter' or command == 'Change':
            nickname = parts[2]
            memo[user_id] = nickname

    for record in records:
        parts = record.split()
        command = parts[0]
        user_id = parts[1]

        if command == 'Enter':
            answer.append(f"{memo[user_id]}님이 들어왔습니다.")
        elif command == 'Leave':
            answer.append(f"{memo[user_id]}님이 나갔습니다.")

    return answer
