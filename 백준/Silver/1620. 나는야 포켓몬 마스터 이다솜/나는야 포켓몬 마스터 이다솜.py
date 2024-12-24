import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}

for i in range(1, n+1):
    word = input().rstrip()
    memo[i] = word
    memo[word] = i

for i in range(m):
    word = input().rstrip()
    if word.isdigit():
        print(memo[int(word)])
    else:
        print(memo[word])