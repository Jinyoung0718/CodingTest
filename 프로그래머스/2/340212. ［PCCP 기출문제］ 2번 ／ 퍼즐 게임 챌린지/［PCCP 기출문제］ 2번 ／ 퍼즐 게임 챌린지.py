def ok(diffs, times, limit, level):
    n = len(diffs)
    total_time = 0

    # diffs[0] = 1이고 숙련도 level은 최소 1로 가정
    total_time += times[0]
    if total_time > limit:
        return False

    for i in range(1, n):
        cur_d = diffs[i]
        cur_t = times[i]
        prev_t = times[i - 1]
        
        if cur_d <= level:
            total_time += cur_t
        else:
            k = cur_d - level
            # k * (t + times[i-1])는 전부 실패한 시도들, 마지막 + t는 성공 시도
            total_time += k * (cur_t + prev_t) + cur_t

        if total_time > limit:
            return False

    return True


def solution(diffs, times, limit):
    # 1 ≤ times[i] ≤ 10,000
    start = 1
    end = 10**6
    answer = end

    while start <= end:
        mid = (start + end) // 2
        if ok(diffs, times, limit, mid):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer