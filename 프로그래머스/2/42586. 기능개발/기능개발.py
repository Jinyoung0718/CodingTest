from collections import deque

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1  # 완료된 작업 개수 증가
        else:
            if count > 0:
                answer.append(count)  # 완료된 작업 수 기록
                count = 0
            time += 1  # 하루 경과
    
    # 마지막으로 남은 작업 개수 추가
    if count > 0:
        answer.append(count)
    
    return answer
