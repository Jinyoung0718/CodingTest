def solution(n, wires):
    answer = float('inf')
    graph = [[] for _ in range(n + 1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(node, parent):
        nonlocal answer
        count = 1
        
        for next_node in graph[node]:
            if next_node == parent:
                continue
            
            child_count = dfs(next_node, node)
            diff = abs(n - (2 * child_count))
            answer = min(answer, diff)
            count += child_count
        
        return count

    dfs(1, 0)
    
    return answer