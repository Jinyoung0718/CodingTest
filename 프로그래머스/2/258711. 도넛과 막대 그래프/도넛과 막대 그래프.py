def solution(edges):
    answer = [0, 0, 0, 0] # 생성 정점, 도넛, 막대, 8자
    max_val = max(map(max, edges))
    in_cnt = [0] * (max_val + 1)
    out_cnt = [0] * (max_val + 1)
        
    for start, end in edges:
        out_cnt[start] += 1 # 진출 차수
        in_cnt[end] += 1    # 진입 차수
        
    for now_node in range(1, max_val + 1):
        
        # 다른 노드로 진입하지 않고, 양방향으로 진출하는 노드: 생성 노드
        if in_cnt[now_node] == 0 and out_cnt[now_node] >= 2:
            answer[0] = now_node 
            
        # 다른 노드로 1번 이상 진입하고 다른 곳으로 진출하지 않음: 막대 그래프
        elif in_cnt[now_node] >= 1 and out_cnt[now_node] == 0:
            answer[2] += 1
        
        # 다른 노드로 2번 이상 진입하고 다른 곳으로 2번 이상 진출함: 8자 그래프
        elif in_cnt[now_node] >= 2 and out_cnt[now_node] == 2: 
            answer[3] += 1
    
    # 생성 정점의 진출 차수 - (막대 개수 + 8자 개수): 도넛 그래프
    answer[1] = out_cnt[answer[0]] - sum(answer[2:])
    
    return answer