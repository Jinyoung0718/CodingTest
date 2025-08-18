def solution(N, stages):
    answer = []
    
    count = [0] * (N + 2)
    for stage in stages:
        count[stage] += 1

    total = len(stages)
    
    for stage in range(1, N + 1):
        if total == 0:
            fail = 0
            
        else:
            fail = count[stage] / total
        
        answer.append((fail, stage))
        total -= count[stage]  # 다음 스테이지로 넘어갈 '도달 인원' 갱신

    answer.sort(key=lambda x: (-x[0], x[1]))
    
    return [s for _, s in answer]