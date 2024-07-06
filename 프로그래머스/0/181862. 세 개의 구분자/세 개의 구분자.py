def solution(myStr):
    a = myStr.replace("a", ' ')
    b = a.replace("b", ' ')
    c = b.replace("c", ' ')
    
    return c.split() if c.split() else ["EMPTY"]