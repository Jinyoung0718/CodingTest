word = input()
memo = {}

for n in word:
    memo[n] = memo.get(n, 0) + 1

mid = ""
flag = 0

for key in memo:
    if memo[key] % 2 != 0:
        memo[key] -= 1
        mid = key
        flag += 1
    if flag == 2:
        print("I'm Sorry Hansoo")
        exit()

first_half = "".join(key * (memo[key] // 2) for key in sorted(memo.keys()))
answer = first_half + mid + first_half[::-1]
print(answer)
