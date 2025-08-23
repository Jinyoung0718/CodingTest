def solution(edges):
    answer = [0, 0, 0, 0] # 생성 정점, 도넛, 막대, 8자
    max_val = max(map(max, edges)) + 1  # +1 은 인덱스 맞춰주기 위함
    in_cnt = [0] * max_val
    out_cnt = [0] * max_val
        
    # in, out 간선 저장
    for start, end in edges:
        out_cnt[start] += 1
        in_cnt[end] += 1
        
    for now_node in range(1, max_val):
        if in_cnt[now_node] == 0 and out_cnt[now_node] >= 2:    # 생성 노드
            answer[0] = now_node 
            
        elif in_cnt[now_node] >= 1 and out_cnt[now_node] == 0:  # 막대 그래프
            answer[2] += 1
            
        elif in_cnt[now_node] >= 2 and out_cnt[now_node] == 2:  # 8자 그래프 
            answer[3] += 1
            
    answer[1] = out_cnt[answer[0]] - sum(answer[2:])            # 도넛 그래프
    
    return answer