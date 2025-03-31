def prime(num):
    if num == 1: return False
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0: return False
    return True

m, n = map(int, input().split())

for i in range(m, n + 1):
    if prime(i):
        print(i)