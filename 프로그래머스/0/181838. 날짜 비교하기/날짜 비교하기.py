def solution (date1, date2):
    a, b, c = date1
    q, w, e = date2
    
    if (a, b, c) < (q, w, e):
        return 1
    elif (a, b, c) > (q, w, e):
        return 0
    else:
        return 0