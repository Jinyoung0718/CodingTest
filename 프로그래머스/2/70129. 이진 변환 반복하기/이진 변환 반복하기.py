def solution(s):
    
    delete_zero = 0
    count = 0
    word = ""
    
    while s != "1":
        
        zeros = s.count("0")
        delete_zero += zeros
        
        s = s.replace("0", "")
        length = len(s)
        s = bin(length)[2:]
        count += 1
        
    return [count, delete_zero]