import math

def solution(k, d):
    count = 0
    
    for x in range(0, d+1, k):
        
        # y 최대값이 실수일 수 있으므로, int로 내림 처리하여 원 내부에 포함되는 가장 큰 정수
        max_y = int(math.sqrt(d**2 - x**2))
        
        # y=0을 포함하기 위해서 + 1을 함
        count += (max_y // k) + 1
    
    return count