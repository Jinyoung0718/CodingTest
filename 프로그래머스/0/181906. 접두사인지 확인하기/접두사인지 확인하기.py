def solution(mys, is_prefix):
    
    for i in range(len(mys)):
        if mys[:i+1] == is_prefix:
            return 1
    return 0