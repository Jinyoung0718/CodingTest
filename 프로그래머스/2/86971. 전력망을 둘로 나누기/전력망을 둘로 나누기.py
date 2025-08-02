def solution(n, wires):
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    min_diff = n

    def dfs(node, parent):
        nonlocal min_diff
        size = 1  # 자기 자신 포함
        for neighbor in graph[node]:
            if neighbor != parent:
                subtree_size = dfs(neighbor, node)
                diff = abs(n - 2 * subtree_size)
                min_diff = min(min_diff, diff)
                size += subtree_size
        return size

    dfs(1, -1)  # 루트를 1로 잡고 시작
    return min_diff

    
    