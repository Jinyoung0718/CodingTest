from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    for perm in permutations(dungeons):
        cleared = 0
        cur_fatigue = k # 현재 피로도 -> 순회해야 함으로 복사
        
        for required, consumed in perm:
            
            if cur_fatigue < required:
                break
            
            cur_fatigue -= consumed
            cleared += 1
        
        answer.append(cleared)
    
    return max(answer)
