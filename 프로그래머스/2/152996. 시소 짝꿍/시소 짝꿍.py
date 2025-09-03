from collections import Counter
from itertools import combinations

def solution(weights):
    answer = 0
    count = Counter(weights)
    distances = [2, 3, 4]

    for w in count:
        if count[w] > 1:
            # n개 중에 2개(짝)을 구할 수 있는 경우의 수 -> nC2
            answer += count[w] * (count[w] - 1) // 2
    
    # 다른 무게끼리 (거리 비율 맞는 경우)
    for a, b in combinations(distances, 2):
        for w in count:
            #내 무게 w, 자리 거리 a에 앉았을 때 상대방이 b에 앉으면 그 사람이 가져야 할 무게가 바로 target
            target = w * b / a
            if target in count:
                answer += count[w] * count[target]
    
    return answer
