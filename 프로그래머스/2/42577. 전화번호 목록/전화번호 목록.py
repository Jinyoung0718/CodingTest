def solution(phone_book):
    memo = {}
    
    # 전화번호를 해시 테이블에 저장
    for num in phone_book:
        memo[num] = True
    
    # 각 전화번호의 접두사를 검사
    for num in phone_book:
        temp = ""
        for i in range(len(num)):
            temp += num[i]
            if temp in memo and temp != num:
                return False
    
    return True
