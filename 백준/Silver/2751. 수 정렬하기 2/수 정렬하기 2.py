import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s, e):
    if e - s < 1: return

    m = int(s+(e-s) // 2)
    merge_sort(s, m)
    merge_sort(m+1, e)

    for i in range(s, e+1):
        temp[i] = A[i]
    
    k = s

    index1 = s
    index2 = m+1


    while index1 <= m and index2 <= e:
        if temp[index1] > temp[index2]:
            A[k] = temp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = temp[index1]
            k += 1
            index1 += 1

    while index1 <= m:
        A[k] = temp[index1]
        k += 1
        index1 += 1

    while index2 <= e:
        A[k] = temp[index2]
        k += 1
        index2 += 1

N = int(input())

A = [0] * int(N+1)
temp = [0] * int(N+1)

for i in range(1, N+1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + '\n')