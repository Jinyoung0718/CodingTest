def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        schedule = time_to_minute(schedules[i]) + 10
        timelog = timelogs[i]
        cur_day = startday - 1
        late = False

        for log in timelog:
            cur_day += 1
            
            if cur_day % 7 in (0, 6):
                continue

            if time_to_minute(log) > schedule:
                late = True
                break

        if not late:
            answer += 1
        
    return answer
            
def time_to_minute(time):
    h = time // 100 # 앞에 두 개
    m = time % 100  # 뒤에 두 개
    return (h * 60) + m