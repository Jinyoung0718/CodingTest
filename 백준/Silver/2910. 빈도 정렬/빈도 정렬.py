n, c = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

memo = {}

for num in arr:
    memo[num] = memo.get(num, 0) + 1

sort_memo = sorted(memo.items(), key=lambda x: (-x[1]))

for key, freq in sort_memo:
    answer.extend([key] * freq)

print(*answer)