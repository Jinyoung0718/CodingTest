n = int(input())
memo = {}

for _ in range(n):
    name = input()
    memo[name[0]] = memo.get(name[0], 0) + 1

answer = [key for key, value in memo.items() if value >= 5]
answer.sort()

if answer:
    print("".join(map(str, answer)))
elif len(answer) < 5:
    print("PREDAJA")