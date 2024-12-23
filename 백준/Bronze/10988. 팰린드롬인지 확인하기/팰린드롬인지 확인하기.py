word = input()
mid = len(word) // 2

if len(word) % 2 != 0:
    if word[:mid] == word[mid+1:][::-1]:
        print(1)
    else:
        print(0)
else:
    if word[:mid] == word[mid:][::-1]:
        print(1)
    else:
        print(0)