def solution(nums):
    answer = []
    memo = {}
    
    for num in nums:
        memo[num] = True
        if num not in answer:
            if len(answer) != (len(nums) // 2):
                answer.append(num)
                
    
    return len(answer)