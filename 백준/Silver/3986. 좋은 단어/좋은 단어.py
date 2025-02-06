n = int(input())
answer = 0

for _ in range(n):
    word = input()
    stack = []
    for v in word:
        if stack and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
    if not stack:
        answer += 1

print(answer)