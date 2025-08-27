def solution(N, stages):
    answer = []
    players = len(stages)
    count = [0] * (N + 2)
    
    # 사용자들이 현재 머물고 있고 클리어하지 못한 스테이지
    for stage in stages:
        count[stage] += 1
    
    for stage in range(1, N + 1):
        
        if players == 0:
            fail = 0    
        else:
            fail = count[stage] / players
        
        answer.append((fail, stage)) # 위험도, 스테이지 넘버
        players -= count[stage]  # 다음 스테이지로 넘어갈 '도달 인원' 갱신

    answer.sort(key=lambda x: (-x[0], x[1]))
    
    return [s for _, s in answer]