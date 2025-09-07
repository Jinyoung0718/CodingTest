from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    len1 = len2 = len(queue1)
    queue1_sum, queue2_sum = sum(queue1), sum(queue2)
    half_total = (queue1_sum + queue2_sum) // 2

    answer = 0
    while queue1_sum != queue2_sum:
        # 더 이상 옮길 게 없거나, 이미 충분히 시도했는데도 답이 안 나오면 불가능
        if len1 == 0 or len2 == 0 or answer > (len1 + len2) * 2:
            return -1

        if queue1_sum < queue2_sum:
            minus = queue2.popleft()
            queue1.append(minus)

            len1 += 1
            len2 -= 1
            queue1_sum += minus
            queue2_sum -= minus
        else:
            minus = queue1.popleft()
            queue2.append(minus)

            len1 -= 1
            len2 += 1
            queue1_sum -= minus
            queue2_sum += minus

        answer += 1

    return answer