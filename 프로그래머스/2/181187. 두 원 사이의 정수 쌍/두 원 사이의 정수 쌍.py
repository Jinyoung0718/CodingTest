import math

# y^2 = r^2 - i^2
def solution(r1, r2):
    answer = 0
    
    # x 좌표를 # 1 ~ r2, 즉 끝까지 순회
    for x in range(1, r2+1):
        
        # x좌표가 작은 원 안쪽이면 시작 값을 올림으로 구함
        if x < r1 :
            start = math.ceil(math.sqrt((r1**2 - x**2)))
            
        # x좌표가 작은 원 밖이면 시작 값은 0
        else : 
            start = 0

        # x=i인 세로줄에서 원과 만나는 y좌표의 절댓값
        end = int(math.sqrt((r2**2 - x**2)))
        answer = answer + (end - start + 1)

    return answer * 4