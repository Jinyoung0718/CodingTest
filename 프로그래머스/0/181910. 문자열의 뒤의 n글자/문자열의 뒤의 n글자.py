def solution(my_string, n):
    lis = list(my_string)
    return ''.join(lis[-n:])