def solution(n, costs):
    
    costs.sort(key = lambda x: x[2])
    union_list = [i for i in range(n)]
    answer = 0
    
    def find(node):
        if union_list[node] != node:
            union_list[node] = find(union_list[node])
        
        return union_list[node]
    
    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)
        
        if parent_a != parent_b:
            union_list[parent_a] = parent_b
            return True
        
        return False
    
    for a, b, cost in costs:
        if union(a, b):
            answer += cost
    
    return answer