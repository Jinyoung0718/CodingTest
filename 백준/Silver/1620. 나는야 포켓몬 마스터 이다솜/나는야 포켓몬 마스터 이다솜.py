n, m = map(int, input().split())
str_memo = {}
int_memo = {}
for i in range(1, n+1):
    word = input()
    str_memo[word] = i
    int_memo[i] = word


word = [input() for _ in range(m)]

for n in word:
    if n in str_memo:
        print(str_memo[n])
    else:
        print(int_memo[int(n)])