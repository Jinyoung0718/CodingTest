def solution(my_string, is_suffix):
    
    for i in range (len(my_string)):
        temp = my_string[-i:]
        if temp == is_suffix:
            return 1
    return 0