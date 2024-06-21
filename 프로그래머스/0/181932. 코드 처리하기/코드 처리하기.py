def solution(code):
    
    mode = 0
    result = ""
    
    for i in range(0, len(code)):
        if mode == 0:
            if code[i] == '1':
                mode = 1 - mode
            else:
                if i % 2 == 0:
                    result += code[i]
        else:
            if code[i] == '1':
                mode = 1 - mode
            else:
                if i % 2 != 0:
                    result += code[i]
                    
    return result if result else "EMPTY"
                    