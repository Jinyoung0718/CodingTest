n = int(input())
result = 0

for _ in range(n):
    sentence = input()
    find = True
    previous = ""
    seen = set()

    for i in sentence:
        if i != previous:
            if i in seen:
                find = False
                break
            seen.add(i)
        previous = i
    
    if find:
        result += 1

print(result)