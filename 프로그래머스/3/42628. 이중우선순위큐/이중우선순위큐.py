import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    # 각 원소가 유효한지 체크할 리스트(인덱스 기반)를 만듭니다.
    valid = [False] * len(operations)
    idx = 0  # 삽입될 때마다 부여할 고유 인덱스
    
    # 모든 연산을 처리합니다.
    for op in operations:
        op_type, num_str = op.split()
        num = int(num_str)
        
        if op_type == 'I':  # 삽입 연산
            # 최소 힙에는 (값, 인덱스), 최대 힙에는 (-값, 인덱스)를 저장합니다.
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            valid[idx] = True  # 이 인덱스의 원소는 유효함을 표시
            idx += 1
        else:  # 삭제 연산
            if num == 1:
                if max_heap:  # 유효한 원소가 있으면
                    _, i = heapq.heappop(max_heap)
                    valid[i] = False  # 해당 원소를 삭제 처리
            else:  # num == -1, 최솟값 삭제
                # 최소 힙의 루트가 유효할 때까지
                if min_heap:
                    _, i = heapq.heappop(min_heap)
                    valid[i] = False

    # 최종 결과 반환 전에, 두 힙 모두에서 삭제된 원소들을 제거합니다.
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
        
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    # 큐가 비었다면 [0, 0] 반환
    if not min_heap or not max_heap:
        return [0, 0]
    
    # 최소 힙의 루트는 최솟값, 최대 힙의 루트의 음수는 최댓값입니다.
    return [-max_heap[0][0], min_heap[0][0]]

