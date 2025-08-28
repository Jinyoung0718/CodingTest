def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0
    total = sequence[0]
    candidates = []

    while left < n and right < n:
        if total == k:
            candidates.append([left, right])
            total -= sequence[left]
            left += 1

        elif total < k:
            right += 1
            if right == n:  # 더 늘릴 수 없음
                break
            total += sequence[right]

        else:  # total > k
            total -= sequence[left]
            left += 1

    # 조건: 길이 짧은 순, 같으면 시작 인덱스 작은 순
    candidates.sort(key=lambda x: (x[1]-x[0], x[0]))
    return candidates[0]
