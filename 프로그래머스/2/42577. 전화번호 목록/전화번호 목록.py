def solution(phone):
    phone.sort()
    temp = ""
    
    for i in range(1, len(phone)):
        if phone[i].startswith(phone[i-1]):
            return False
    
    return True