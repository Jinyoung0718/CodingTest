alpha = {}
alphabet = 97
for i in range(1, 27):
    alpha[chr(alphabet)] = i
    alphabet += 1

n = int(input())
word = input()
result = 0
multiple = 0
for n in word:
    result += alpha[n]*(31**multiple)
    multiple += 1
print(result)