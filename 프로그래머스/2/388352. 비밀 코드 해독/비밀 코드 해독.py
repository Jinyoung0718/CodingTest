from itertools import combinations

def solution(n, q, ans):
    
    # 1~n까지 숫자 중 5개 조합 전부
    all_codes = combinations(range(1, n + 1), 5)
    count = 0
    
    for code in all_codes:
        valid = True
        code_set = set(code)
        
        for query, expected in zip(q, ans):
            inter = len(code_set & set(query))
            if inter != expected:
                valid = False
                break
        
        if valid:
            count += 1
    
    return count
