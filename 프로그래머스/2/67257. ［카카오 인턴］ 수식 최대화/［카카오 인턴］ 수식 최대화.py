from itertools import permutations

def parse(expression):
    nums = []
    ops = []
    num = ''
    
    for c in expression:
        if c not in '+-*':
            num += c
        else:
            nums.append(int(num))
            ops.append(c)
            num = ''
            
    nums.append(int(num))
    
    return nums, ops


def calc(nums, ops, priority):
    nums = nums[:]
    ops = ops[:]

    for op in priority:
        i = 0
        
        while i < len(ops):
            if op == ops[i]:
                if op == '+':
                    val = nums[i] + nums[i + 1]
            
                elif op == '-':
                    val = nums[i] - nums[i + 1]
                    
                elif op == '*':
                    val = nums[i] * nums[i + 1]
                    
                nums[i] = val
                del nums[i + 1]
                del ops[i]    
            else:
                i += 1
                
    return abs(nums[0])


def solution(expression):
    nums, ops = parse(expression)
    operations = set(ops)
    max_result = 0

    for op_order in permutations(operations):
        result = calc(nums, ops, op_order)
        max_result = max(max_result, result)

    return max_result