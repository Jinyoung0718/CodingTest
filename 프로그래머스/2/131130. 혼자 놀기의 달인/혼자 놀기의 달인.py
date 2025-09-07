def solution(cards):
    n = len(cards)
    visited = set()
    answer = []
    
    def dfs(x):
        count = 1
        visited.add(x)
        next_card = cards[x] - 1
        
        if next_card not in visited:
            count += dfs(next_card)
        
        return count
    
    for i in range(n):
        if i not in visited:
            answer.append(dfs(i))
    
    if len(answer) < 2:
        return 0
    
    answer.sort(reverse = True)
    return answer[0] * answer[1]