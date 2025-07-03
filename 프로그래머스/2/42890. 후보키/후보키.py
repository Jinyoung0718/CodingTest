from itertools import combinations

def solution(relation):
    num_cols = len(relation[0])
    num_rows = len(relation)

    candidates = []

    for i in range(1, num_cols + 1):
        for comb in combinations(range(num_cols), i):
            # 유일성 검사
            projection = [tuple(item[c] for c in comb) for item in relation]
            if len(set(projection)) != num_rows:
                continue

						# 최소성 검사
            is_minimal = True
            
            for c in candidates:
                if set(c).issubset(comb):
                    is_minimal = False
                    break

            if is_minimal:
                candidates.append(comb)

    return len(candidates)
