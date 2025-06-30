from itertools import combinations

def solution(orders, course):
    
    answer = []
    
    for c in course:
        memo = {}
        
        for order in orders:
            sorted_order = sorted(order)
            combs = combinations(sorted_order, c)
            
            for comb in combs:
                key = ''.join(comb)
                
                if key not in memo:
                    memo[key] = 1
                else:
                    memo[key] += 1
        
        if memo:
            max_count = max(memo.values())
            if max_count >= 2:
                for key, val in memo.items():
                    if val == max_count:
                        answer.append(key)
    
    return sorted(answer)