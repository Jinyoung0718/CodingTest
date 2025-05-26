def solution(nums):
    memo = {}
    answer = 0
    temp = len(nums) // 2
    
    for num in nums:
        memo[num] = memo.get(num, 0) + 1
    
    if len(memo) < temp:
        return len(memo)
    else:
        return temp