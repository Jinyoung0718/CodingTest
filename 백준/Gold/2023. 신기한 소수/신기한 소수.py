import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

def is_prime(num):
    if num == 1: return False
    for su in range(2, int(num**(1/2)) + 1):
        if num % su == 0: return False
    return True

def dfs(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1, 10, 2):
            new_number = number * 10 + i
            if is_prime(new_number):
                dfs(new_number)

dfs(2)
dfs(3)
dfs(5)
dfs(7)