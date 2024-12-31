def solution(phone):
    phone.sort()
    
    temp = phone[0]
    for num in phone[1:]:
        if num.startswith(temp):
            return False
        
        temp = num
    return True