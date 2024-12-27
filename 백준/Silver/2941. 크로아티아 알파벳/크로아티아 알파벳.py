memo = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
i = 0
answer = 0

while i < len(word):
    for m in memo:
        if word[i:i+len(m)] == m:
            answer += 1
            i += len(m)
            break
    else:
        answer += 1
        i += 1

print(answer)