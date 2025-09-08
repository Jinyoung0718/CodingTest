from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    max_ops = (len(queue1) + len(queue2)) * 2

    while queue1_sum != queue2_sum:
        if answer > max_ops:
            return -1

        if queue1_sum < queue2_sum:
            minus = queue2.popleft()
            queue1.append(minus)
            
            queue1_sum += minus
            queue2_sum -= minus
        elif queue1_sum > queue2_sum:
            minus = queue1.popleft()
            queue2.append(minus)
            
            queue1_sum -= minus
            queue2_sum += minus

        answer += 1

    return answer