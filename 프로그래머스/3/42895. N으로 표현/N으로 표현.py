def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]  # dp[1] ~ dp[8] 사용 (인덱스 0은 사용 안 함)

    for i in range(1, 9):  # N 사용 횟수: 1개부터 8개까지
        # 같은 숫자를 i번 반복해서 만든 수 (예: 5, 55, 555 ...)
        dp[i].add(int(str(N) * i))

        for j in range(1, i):  # i를 두 덩어리로 쪼갬
            for x in dp[j]:       # 앞쪽 덩어리에서 만든 숫자
                for y in dp[i - j]:  # 뒤쪽 덩어리에서 만든 숫자
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)

        # 목표 수가 현재 dp[i] 안에 있으면 사용 횟수 i가 최소
        if number in dp[i]:
            return i

    return -1  # 8번 이내로 표현 불가능한 경우

