def solution(k, tangerine):
    answer = 0
    memo = {}
    
    for n in tangerine:
        memo[n] = memo.get(n, 0) + 1
    
    # 크기 별 "갯수"를 내림차순 정렬 -> 해시이기에 중복 문제 없음
    counts = sorted(memo.values(), reverse=True)
    
    for c in counts:
        if k <= 0:
            break
        k -= c
        answer += 1
    
    return answer