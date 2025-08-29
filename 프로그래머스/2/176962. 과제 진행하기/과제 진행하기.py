def time_to_min(time):
    hour, minute = map(int, time.split(":"))
    return (hour * 60) + minute

def solution(plans):
    answer = []
    stack = []
    
    jobs = []
    for subject, start_time, process_time in plans:
        jobs.append([subject, time_to_min(start_time), int(process_time)])
    
    # 시작 시각 오름차순 정렬
    jobs.sort(key = lambda x: x[1])
    cur_time = jobs[0][1]

    
    for subject, start_time, process_time in jobs:
        
        # 현재 스택(진행/멈춤 과제)을 다음 과제 시작 시각까지 최대한 처리
        while stack and cur_time < start_time:
            cur_subject, cur_process_time = stack.pop()
            gap = start_time - cur_time
            
            # 이 과제를 다 끝낼 수 있음
            if cur_process_time <= gap:
                cur_time += cur_process_time
                answer.append(cur_subject)
                
            # 다 못 끝냄 -> 남은 시간 갱신하고 다시 스택에
            else:
                cur_process_time -= gap
                cur_time = start_time
                stack.append([cur_subject, cur_process_time])
                break
                
        # 새 과제 시작(규칙상 새 과제가 우선)
        cur_time = max(cur_time, start_time)
        stack.append([subject, process_time])

    while stack:
        subject, remain_time = stack.pop()
        cur_time += remain_time
        answer.append(subject)

    return answer