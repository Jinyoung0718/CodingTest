def solution(diffs, times, limit):
    n = len(diffs)

    # 주어진 level에서 총 소요 시간이 limit 이하인지 검사
    def ok(level):
        total = 0

        # 0번 퍼즐: diffs[0] = 1 (문제 보장) → level ≥ 1 이므로 항상 한 번에 통과
        total += times[0]
        if total > limit:
            return False

        i = 1
        while i < n:
            d = diffs[i]
            t = times[i]
            if d <= level:
                total += t
            else:
                k = d - level  # 틀리는 횟수
                total += k * (t + times[i - 1]) + t
            if total > limit:  # 가지치기
                return False
            i += 1

        return True

    start = 1
    end = 100000
    answer = end

    while start <= end:
        mid = (start + end) // 2
        if ok(mid):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer