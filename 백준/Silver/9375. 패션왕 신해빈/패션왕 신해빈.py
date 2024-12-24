import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    memo = {}
    for _ in range(n):
        cloth, type = input().split()
        memo[type] = memo.get(type, 1) + 1

    answer = 1
    for type in memo:
        answer *= memo[type]

    print(answer - 1)