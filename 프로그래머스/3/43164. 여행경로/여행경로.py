import heapq
from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    route = []
    
    for a, b in tickets:
        heapq.heappush(graph[a], b) # 목적지를 사전순(min-heap)으로 관리
    
    def dfs(start_airport):
        while graph[start_airport]:
            dfs(heapq.heappop(graph[start_airport])) # 사전순으로 가장 작은 목적지부터 소모
            
        route.append(start_airport) # 더 갈 곳이 없을 때 경로에 추가 (역순 쌓임 -> 목적지 부터 쌓임)

    dfs("ICN")
    return route[::-1]  # 역순 반환