import sys
input = sys.stdin.readline

def roundup(x):
    return int(x + 0.5)

n = int(input())
if n == 0:
    print(0)
    exit()

arr = [int(input()) for _ in range(n)]
arr.sort()

cut = roundup(n * 0.15)
trimmed = arr[cut : n - cut]

average = sum(trimmed) / len(trimmed)
print(roundup(average))
