def solution(cards):
    n = len(cards)
    visited = [False] * n
    group_sizes = []
    
    def dfs(cur):
        visited[cur] = True
        count = 1
        next_card = cards[cur] - 1 # 박스 안의 적힌 다음 상자 인덱스
        
        if not visited[next_card]:
            count += dfs(next_card)
        
        return count
    
    for i in range(n):
        if not visited[i]:
            group_sizes.append(dfs(i))
    
    if len(group_sizes) < 2:
        return 0
    
    group_sizes.sort(reverse=True)
    return group_sizes[0] * group_sizes[1]