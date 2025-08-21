def solution(players, m, k):
    answer = 0
    
    # 각 시각별 만료될 수용 가능 인원 기록
    servers = [0] * (24 + k)
    capacity = m
    
    for time, player in enumerate(players):
        
        # 만료된 서버 수용력 차감
        capacity -= servers[time]
        
        if capacity <= player:
            add_servers = ((player - capacity) // m) + 1
            answer += add_servers
            capacity += add_servers * m
            
            # k시간 뒤 만료될 수용력을 기록
            servers[time + k] += add_servers * m
    
    return answer
