word = input()
result = []

for w in word:
    if 'A' <= w <= 'Z' or 'a' <= w <= 'z':
        if 77 < ord(w) <= 90 or 109 < ord(w) <= 122:
            result.append(chr(ord(w) - 13))
        else:
            result.append(chr(ord(w) + 13))
    else:
        result.append(w)

print("".join(map(str, result)))