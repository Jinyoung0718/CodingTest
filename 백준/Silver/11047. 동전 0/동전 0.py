n, k = map(int, input().split())
A = [0] * n
result = 0

for i in range(n):
    A[i] = int(input())


for i in range(n - 1, -1, -1):
    if A[i] <= k:
        result += (k // A[i])
        k = (k % A[i])

print(result) 