import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

result = 0

for i in range(n):
    find = A[i]
    left = 0
    right = n - 1

    while left < right:
        if A[left] + A[right] < find:
            left += 1
        elif A[left] + A[right] > find:
            right -= 1
        else:
            if left != i and right != i:
                result += 1
                break
            elif left == i:
                left += 1
            elif right == i:
                right -= 1
print(result)