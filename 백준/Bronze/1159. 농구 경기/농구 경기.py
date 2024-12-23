n = int(input())
memo = {}

for i in range(n):
    word = input()
    if word[0] in memo:
        memo[word[0]] += 1
        continue
    memo[word[0]] = 1

result = [key for key, value in memo.items() if value >= 5]
result.sort()
if result:
    print("".join(map(str, result)))
else:
    print("PREDAJA")