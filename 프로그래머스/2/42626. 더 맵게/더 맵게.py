import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 최소 힙 변환
    answer = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)  # 가장 작은 값
        second = heapq.heappop(scoville)  # 두 번째 작은 값
        new_scoville = first + (second * 2)  # 새로운 음식의 스코빌 지수
        heapq.heappush(scoville, new_scoville)  # 힙에 추가
        answer += 1  # 섞은 횟수 증가
    
    # 모든 음식의 스코빌 지수가 K 이상인지 확인
    return answer if scoville[0] >= K else -1
