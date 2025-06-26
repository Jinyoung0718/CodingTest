def solution(prices):
    answer = []
    n = len(prices)

    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            count += 1
            if prices[i] > prices[j]:  # 가격이 떨어진 순간
                break
        answer.append(count)

    return answer