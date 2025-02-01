def solution(nums):
    temp = len(nums) // 2
    set_nums = set(nums)
    
    if len(set_nums) > temp:
        return temp
    else:
        return len(set_nums)