def solution(phone_book):
    memo = {}
    
    for num in phone_book:
        memo[num] = True
    
    for num in phone_book:
        temp = ""
        for i in range(len(num)):
            temp += num[i]
            if temp in memo and temp != num:
                return False
    
    return True