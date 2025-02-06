def check_word(word):
    dic = {'a', 'e', 'i', 'o', 'u'}
    vowel = 0
    consonant = 0
    has_vowel = False
    prev = ""

    for n in word:
        if n in dic:
            has_vowel = True
            vowel += 1
            consonant = 0
        else:
            consonant += 1
            vowel = 0

        if consonant >= 3 or vowel >= 3:
            return False

        if prev == n and n not in {'e', 'o'}:
            return False

        prev = n
    return has_vowel
while True:
    word = input()
    if word == 'end':
        break

    if check_word(word):
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')