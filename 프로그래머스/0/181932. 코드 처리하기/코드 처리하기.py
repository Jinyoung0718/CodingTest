def solution(code):
    
    mode = 0
    result = ""
    
    for i in range(0, len(code)):
        if code[i] == "1":
            mode = 1 - mode
        if mode == 0 and code[i] != "1":
            if i % 2 == 0 :
                result += code[i]
        elif mode == 1 and code[i] != "1":
            if i % 2 !=0 :
                result += code[i]
                
    return result if result else "EMPTY"
                