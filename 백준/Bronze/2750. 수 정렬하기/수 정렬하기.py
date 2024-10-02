import sys

input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]

for i in range(n-1):
    for j in range(n-1-i):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(n):
    print(A[i])