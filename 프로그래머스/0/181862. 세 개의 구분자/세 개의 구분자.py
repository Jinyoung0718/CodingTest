def solution(myStr):
    result = []
    
    for i in ['a', 'b','c']:
        myStr = myStr.replace(i, ' ')
    result = myStr.split()
    if not result:
        result = ["EMPTY"]
    return result