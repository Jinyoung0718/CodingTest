from collections import Counter
word_list = list(input())
word_list.sort()

word_count = Counter(word_list)

odd_alphabet_count = 0
odd_alphabet = ''

for alphabet in word_count:
    if word_count[alphabet] % 2 == 1:
        odd_alphabet_count += 1
        odd_alphabet += alphabet
    if odd_alphabet_count > 1:
        print("I'm Sorry Hansoo")
        exit()

answer = ''

for i in range(0, len(word_list), 2):
    if word_count[word_list[i]] % 2 == 1:
        word_count[word_list[i]] -= 1
    else:
        answer += word_list[i]

tmp = answer[::-1]
answer += odd_alphabet
answer += tmp
print(answer)