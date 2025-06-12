from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def solution(numbers):
    number_set = set()
    
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            number_set.add(num)
    
    count = 0
    
    for num in number_set:
        if is_prime(num):
            count += 1
    
    return count