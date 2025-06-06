import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2 and scoville[0] < K:
        i = heapq.heappop(scoville)
        j = heapq.heappop(scoville)
        new = i + (j * 2)
        heapq.heappush(scoville, new)
        answer += 1

    if scoville[0] < K:
        return -1
    
    return answer