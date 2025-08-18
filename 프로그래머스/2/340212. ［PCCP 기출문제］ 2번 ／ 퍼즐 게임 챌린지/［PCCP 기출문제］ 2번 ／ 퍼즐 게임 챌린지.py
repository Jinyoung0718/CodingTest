def solution(diffs, times, limit):
    n = len(diffs)
    lo, hi = 1, max(diffs)  # level은 양의 정수, max(diffs)면 항상 모두 한 번에 통과

    def can(level):
        total = 0
        # 첫 퍼즐: diffs[0] == 1, level >= 1 이므로 항상 한 번에 해결
        total += times[0]
        if total > limit:
            return False
        for i in range(1, n):
            d, t = diffs[i], times[i]
            if d <= level:
                total += t
            else:
                k = d - level
                total += k * (t + times[i - 1]) + t
            if total > limit:  # 가지치기로 시간 단축
                return False
        return total <= limit

    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if can(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans
