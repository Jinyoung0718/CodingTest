n = int(input())
A = list(map(int, input().split()))
A.sort()


count = 0

for i in range(n):
    find = A[i]
    s = 0
    e = n - 1
    while s < e:
        if A[s] + A[e] < find:
            s += 1
        elif A[s] + A[e] > find:
            e -= 1
        else:
            if s != i and e != i:
                count += 1
                break
            elif s == i:
                s += 1
            elif e == i:
                e -= 1
            
print(count)