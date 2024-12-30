def solution(nums):
    choice = len(nums) // 2
    set_num = set(nums)
    
    if len(set_num) > choice:
        return choice
    else:
        return len(set_num)