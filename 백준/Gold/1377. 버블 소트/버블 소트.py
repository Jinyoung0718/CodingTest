import sys
input = sys.stdin.readline

n = int(input())
A = []

for i in range(n):
    A.append((int(input()), i))

max = 0
sorted_A = sorted(A)

for i in range(n):
    if max < sorted_A[i][1] - i: # 두 번째 값이 인덱스이므로, 값 이동을 위해 앞은 i
        max = sorted_A[i][1] - i

print(max + 1)