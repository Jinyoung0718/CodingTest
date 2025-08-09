def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        schedule = convert(schedules[i]) + 10
        timelog = timelogs[i]
        cur_day = startday - 1
        
        for log in timelog:
            cur_day += 1
            if cur_day % 7 in (0, 6):
                continue
        
            if convert(log) > schedule:
                break
        else:
            answer += 1
        
    return answer
            
def convert(time):
    time = str(time)
    h, m = time[:-2], time[-2:]
    return int(h) * 60 + int(m)