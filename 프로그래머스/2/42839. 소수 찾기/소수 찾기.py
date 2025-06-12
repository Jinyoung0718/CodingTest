from itertools import permutations

def sieve(n):
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

def solution(numbers):
    number_set = set()

    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            number_set.add(num)

    max_val = max(number_set)
    is_prime = sieve(max_val)

    return sum(1 for num in number_set if is_prime[num])

