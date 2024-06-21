def solution(num):
    a = 1
    b = 0
    for i in num:
        a *= i
        b += i
    b = b**2
    return 1 if a < b else 0