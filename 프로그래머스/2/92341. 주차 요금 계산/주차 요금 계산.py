from collections import defaultdict
import math

def time_to_minute(time):
    hour, minute = map(int, time.split(':'))
    return (hour * 60) + minute

def solution(fees, records):
    answer = []
    memo = defaultdict(list)

    for word in records:
        time, car_num, status = word.split()
        time_min = time_to_minute(time)
        memo[car_num].append((time_min, status))
    
    for car_num, record in sorted(memo.items(), key=lambda x: x[0]):
        # 입차시간 저장용
        stack = -1
        accure_time = 0
        
        for time_min, status in record:
            if status == "IN":
                stack = time_min
                
            elif status == "OUT":
                accure_time += (time_min - stack)
                stack = -1

        # 출차 안 하고 남아 있는 경우 → 23:59 처리
        if stack != -1:
            accure_time += time_to_minute("23:59") - stack

        # 요금 계산
        if accure_time <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + math.ceil((accure_time - fees[0]) / fees[2]) * fees[3]

        answer.append(fee)

    return answer