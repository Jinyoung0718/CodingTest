def solution(ineq, eq, n, m) :
    
    if ineq == ">":
        if eq == "=":
            return int(n>=m)
        if eq == "!":
            return int(n>m)
        
    if ineq == "<":
        if eq == "=":
            return int(n<=m)
        if eq == "!":
            return int(n<m)
        