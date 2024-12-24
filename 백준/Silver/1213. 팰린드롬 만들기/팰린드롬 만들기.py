from collections import Counter

word_check = Counter(input())
result = ""
odd_alpha = ""
odd_check = 0

for key, val in word_check.items():
    if val % 2 != 0:
        odd_alpha = key
        odd_check += 1
        if odd_check > 1:
            print("I'm Sorry Hansoo")
            exit()

for key, val in sorted(word_check.items()):
    result += (key * (val//2))

print(result + odd_alpha + result[::-1])