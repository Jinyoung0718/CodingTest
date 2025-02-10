import re

test = int(input())
answer = []
for _ in range(test):
    word = input()
    answer.extend(map(int, re.findall(r'\d+', word)))

answer.sort()
print("\n".join(map(str, answer)))