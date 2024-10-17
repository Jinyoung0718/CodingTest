n = input()
count = [0] * 10

for i in range(len(n)):
    num = int(n[i])
    if num == 9 or num == 6:
        if count[6] < count[9]:
            count[6] += 1
        else:
            count[9] += 1
    else:
        count[num] += 1

print(max(count))