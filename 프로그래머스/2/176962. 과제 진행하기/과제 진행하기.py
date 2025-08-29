def time_to_min(time):
    hour, minute = map(int, time.split(":"))
    return (hour * 60) + minute

def solution(plans):
    answer = []
    stack = []
    jobs = sorted([(n, time_to_min(s), int(e)) for n, s, e in plans], key = lambda x : x[1])
    
    cur_time = jobs[0][1]
    
    for subject, start_time, process_time in jobs:
        
        while stack and cur_time < start_time:
            stop_subject, stop_process_time = stack.pop()
            gap = start_time - cur_time
            
            if stop_process_time <= gap:
                cur_time += stop_process_time
                answer.append(stop_subject)
            else:
                stop_process_time -= gap
                cur_time = start_time
                stack.append([stop_subject, stop_process_time])
                break
        
        cur_time= start_time
        stack.append([subject, process_time])
    
    while stack:
        subject, remain_time = stack.pop()
        cur_time += remain_time
        answer.append(subject)
    
    return answer