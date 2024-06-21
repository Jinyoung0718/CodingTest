def solution(a, d, included):
    temp = 0
    result= 0
    
    for i in range(0, len(included)):
        temp = a + (d*i)
        if included[i] == 1:
            result += temp
            
    return result

# +=는 변수에 값을 누적시키는 데 사용되고, =는 변수를 특정 값으로 초기화하거나 재할당하는 데 사용
            