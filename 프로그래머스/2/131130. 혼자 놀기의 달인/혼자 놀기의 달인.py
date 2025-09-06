def solution(cards):
    n = len(cards)
    visited = [False] * n
    group_sizes = []
    
    def dfs(start):
        cnt = 0
        cur = start
        while not visited[cur]:
            visited[cur] = True
            cnt += 1
            cur = cards[cur] - 1  # 다음 상자 (1-based → 0-based)
        return cnt
    
    for i in range(n):
        if not visited[i]:
            size = dfs(i)
            group_sizes.append(size)
    
    # 사이클이 1개뿐이면 점수 = 0
    if len(group_sizes) < 2:
        return 0
    
    group_sizes.sort(reverse=True)
    return group_sizes[0] * group_sizes[1]
