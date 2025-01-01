n, c = map(int, input().split())
arr = list(map(int, input().split()))

memo = {}
answer = []

for num in arr:
    memo[num] = memo.get(num, 0) + 1

sorted_memo = sorted(memo.items(), key=lambda x: (-x[1], arr.index(x[0])))

for key, freq in sorted_memo:
    answer.extend([key] * freq)

print(*answer)