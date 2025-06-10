from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1  # x가 앞에 와야 함
    elif x + y < y + x:
        return 1   # y가 앞에 와야 함
    else:
        return 0

def solution(numbers):
    # 모든 숫자를 문자열로 변환
    numbers_str = list(map(str, numbers))
    
    # 비교 함수 기반으로 정렬
    numbers_str.sort(key=cmp_to_key(compare))
    
    # 예외 처리: [0, 0, 0] -> '0'이 되게
    if numbers_str[0] == '0':
        return '0'
    
    return ''.join(numbers_str)
