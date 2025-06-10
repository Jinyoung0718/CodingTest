n = int(input())
target_sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1
possible = True

for target in target_sequence:
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print("NO")