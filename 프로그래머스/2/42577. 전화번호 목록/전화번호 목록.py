def solution(phone_book):
    phone_book.sort()
    find = True
    temp = phone_book[0]
    
    for i in range(1, len(phone_book)):
        
        if phone_book[i].startswith(temp):
            find = False
            break
        
        temp = phone_book[i]
    
    return find