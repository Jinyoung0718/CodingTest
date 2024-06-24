def solution(my_string, is_suffix):
    result = ""
    
    for i in range(0, len(my_string)):
        result = my_string[-i:]
        if result == is_suffix:
            return 1
    return 0