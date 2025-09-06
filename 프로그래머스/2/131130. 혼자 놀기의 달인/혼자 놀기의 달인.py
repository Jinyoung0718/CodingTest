def solution(cards):
    n = len(cards)
    visited = [False] * n
    group_sizes = []
    
    def dfs(node):
        if visited[node]:
            return 0
        visited[node] = True
        return 1 + dfs(cards[node] - 1)  # 다음 상자로 이동
    
    for i in range(n):
        if not visited[i]:
            group_sizes.append(dfs(i))
    
    if len(group_sizes) < 2:
        return 0
    
    group_sizes.sort(reverse=True)
    return group_sizes[0] * group_sizes[1]

