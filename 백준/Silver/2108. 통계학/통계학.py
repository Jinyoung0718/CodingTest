import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input() )for _ in range(n)]
arr.sort()
memo = {}

for num in arr:
    memo[num] = memo.get(num, 0) + 1

temp = max(memo.values())
answer = []

for key, val in memo.items():
    if val == temp:
        answer.append(key)

answer.sort()
mode = answer[1] if len(answer) > 1 else answer[0]

print(round(sum(arr) / n))
print(arr[n // 2])
print(mode)
print(arr[-1] - arr[0])