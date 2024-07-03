def solution(binomial):
    
    a, op, c = binomial.split()
    
    if op == "+":
        return int(a) + int(c)
    elif op == "-":
        return int(a) - int(c)
    elif op == "*":
        return int(a) * int(c)