def solution(bino):
    
    a, op, b = bino.split()
    
    if op == "+":
        return int(a) + int(b)
    elif op == "-":
        return int(a) - int(b)
    else:
        return int(a) * int(b)
    