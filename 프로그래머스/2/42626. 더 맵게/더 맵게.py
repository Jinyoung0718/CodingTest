import heapq

def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        answer += 1
        most_spicy = heapq.heappop(scoville)
        second_spicy = heapq.heappop(scoville)
        
        new_scovile = most_spicy + (second_spicy * 2)
        # heapq.heappush(힙리스트, 넣을값)
        heapq.heappush(scoville, new_scovile)
    
    if scoville[0] < K:
        answer = - 1
    
    return answer