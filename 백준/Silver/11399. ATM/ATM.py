n = int(input())
A = list(map(int ,input().split()))
A.sort()

result = 0

for i in range(n):
    result += sum(A[:i + 1])

print(result)