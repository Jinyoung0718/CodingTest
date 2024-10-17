from collections import deque

T = int(input())  # 테스트 케이스 수 입력
for _ in range(T):
    total, target = map(int, input().split())  # 문서의 개수와 타겟 문서 위치 입력
    queue = deque(enumerate(map(int, input().split())))  # 중요도와 문서의 인덱스를 저장

    count = 0  # 인쇄 순서를 카운트

    while queue:
        # 현재 큐에서 가장 큰 중요도를 구한다
        current_max_priority = max([doc[1] for doc in queue]) 

        # 첫 번째 문서를 꺼내 확인
        current_doc = queue.popleft()
        
        if current_doc[1] == current_max_priority:  # 가장 큰 중요도라면
            count += 1  # 인쇄 순서를 증가시킨다
            
            if current_doc[0] == target:  # 타겟 문서라면
                print(count)  # 현재 순서를 출력하고 종료
                break
        else:
            queue.append(current_doc)  # 중요도가 낮다면 다시 큐에 넣는다
