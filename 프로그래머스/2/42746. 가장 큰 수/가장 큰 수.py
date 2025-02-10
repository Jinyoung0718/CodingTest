import functools

def comparator(a, b):
    t1 = a + b  
    t2 = b + a  

    if int(t1) > int(t2):
        return -1  # 원래 1을 반환했던 부분을 -1로 변경
    elif int(t1) < int(t2):
        return 1   # 원래 -1을 반환했던 부분을 1로 변경
    else: 
        return 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator))  # reverse=True 제거
    answer = str(int(''.join(n)))
    return answer
