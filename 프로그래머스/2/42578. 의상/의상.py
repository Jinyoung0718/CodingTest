def solution(clothes):
    memo = {}

    for cloth, type in clothes:
        memo[type] = memo.get(type, 0) + 1  # ✅ 정확한 카운팅

    answer = 1
    for count in memo.values():
        answer *= (count + 1)

    return answer - 1  # 공집합 제거
