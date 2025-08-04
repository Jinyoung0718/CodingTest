def solution(n, times):
    left = 1  # 최소 시간
    right = max(times) * n  # 최대 시간 (가장 느린 심사관이 전부 담당하는 경우)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        people = sum(mid // time for time in times)

        if people >= n:
            answer = mid
            right = mid - 1  # 더 짧은 시간으로 가능할 수도 있음 → 왼쪽 탐색
        else:
            left = mid + 1  # 시간 부족 → 오른쪽 탐색

    return answer