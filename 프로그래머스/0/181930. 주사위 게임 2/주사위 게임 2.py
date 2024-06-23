def solution(a, b, c):
    list = [a, b, c]
    q = set(list)
    
    if len(q) == 3:
        return a + b + c
    elif len(q) == 2:
        return  (a + b + c) * (a**2 + b**2 + c**2 )
    elif len(q) == 1:
        return (a + b + c) *  (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
        