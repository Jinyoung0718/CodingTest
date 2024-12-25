alpha = {}
alphabet = 97
for i in range(1, 27):
    alpha[chr(alphabet)] = i
    alphabet += 1

n = int(input())
word = input()
result = 0
multiple = 0
M = 1234567891
r = 31

for char in word:
    result = (result + alpha[char] * (r ** multiple) % M) % M
    multiple += 1

print(result)