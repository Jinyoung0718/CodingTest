from collections import Counter

def solution(topping):
    answer = 0
    
    # 오른쪽 전체 토핑 개수
    right_map = Counter(topping)
    left_map = Counter()
    
    for t in topping:
        
        # 왼쪽에 토핑 추가
        left_map[t] += 1
        
        # 오른쪽에서 토핑 제거
        right_map[t] -= 1
        if right_map[t] == 0:
            del right_map[t]
        
        # 종류 수 비교
        if len(left_map) == len(right_map):
            answer += 1
    
    return answer