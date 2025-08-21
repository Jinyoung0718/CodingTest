def solution(infos, n, m):
    INF = float('inf')

    # dp[a] = A가 a 흔적일 때 B의 최소 흔적
    # dp[2] = 3 → 지금까지 A가 흔적 2를 남겼을 때, 그때까지 B는 최소 3 흔적을 남긴 상태
    dp = [INF] * (n)
    dp[0] = 0

    for info in infos:
        a_trace, b_trace = info
        # 이번 물건을 고려했을 때의 새로운 결과
        new_dp = [INF] * n

        # A 도둑은 최대 n-1 흔적까지만 허용됨 -> 지금까지 A가 남긴 흔적 개수
        for a in range(n):

            # A가 훔치는 경우
            if a + a_trace < n:
                new_dp[a + a_trace] = min(new_dp[a + a_trace], dp[a])

            # B가 훔치는 경우
            if dp[a] + b_trace < m:
                new_dp[a] = min(new_dp[a], dp[a] + b_trace)

        dp = new_dp

    # 가능한 A 흔적 후보들을 모아둠
    candidates = []
    for a in range(n):
        if dp[a] < m:  # B 도둑도 잡히지 않는 경우
            candidates.append(a)

    # 후보가 있으면 그중 최소값, 없으면 INF
    if candidates:
        answer = min(candidates)
    else:
        answer = INF

    return -1 if answer == INF else answer