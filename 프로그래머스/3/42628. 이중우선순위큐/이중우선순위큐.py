import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = [False] * len(operations)  # 각 원소의 유효성 추적

    for i, operation in enumerate(operations):
        op, num = operation.split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
        else:
            if num == 1:  # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                    
            else:         # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

                    
    # 최종 정리: 아직 살아있는 값만 남김
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
        
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]
