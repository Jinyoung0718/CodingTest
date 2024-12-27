n = int(input())
result = 0

for _ in range(n):
    word = input()
    seen = set()
    previous = ""
    find = True

    for w in word:
        if previous != w:
            if w in seen:
                find = False
                break
            seen.add(w)
        previous = w
    
    if find: result += 1

print(result)