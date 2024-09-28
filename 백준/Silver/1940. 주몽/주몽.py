import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
A = list(map(int, input().split()))
A.sort()

count = 0
left = 0
right = n-1

while left < right:
    if A[left] + A[right] < m:
        left += 1
    elif A[left] + A[right] > m:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1

print(count)