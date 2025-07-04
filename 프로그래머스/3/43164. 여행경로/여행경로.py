def solution(tickets):
    answer = []
    graph = {}
    
    for a, b in sorted(tickets):
        if a not in graph:
            graph[a] = []
            
        graph[a].append(b)

    def dfs(airport):
        
        # 공항에서 출발할 수 있는 티켓이 남아 있을 때만 반복
        while airport in graph and graph[airport]:
            
            # 항상 가장 앞(사전순) 노드 선택
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
            
        answer.append(airport)

    dfs("ICN")
    return answer[::-1]  
    # 재귀로 갈 수 있는 공항을 끝까지 추적하고 마지막 요소에서 append를 하므로 역순으로 저장되기에 반대로 출력
