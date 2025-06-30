def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def dfs(cur_node):
        visited[cur_node] = True
        
        for i in range(n):
            if computers[cur_node][i] and not visited[i]:
                dfs(i)   
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer