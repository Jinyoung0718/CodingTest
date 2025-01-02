n = int(input())
result = 0
for _ in range(n):
    sentence = input()
    seen = set()
    previous = ""
    find = True

    for i in sentence:
        if previous != i:
            if i in seen:
                find = False
                break
            seen.add(i)
        previous = i
    
    if find: result += 1

print(result)