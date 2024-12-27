def mod_exp(a, b, c):
    if b == 1:
        return a % c

    result = mod_exp(a, b//2, c)
    result = (result * result) % c

    if b % 2 == 1:
        result = (result * a) % c

    return result

A, B, C = map(int, input().split())
print(mod_exp(A,B,C))