cm = []

for _ in range(9):
    cm.append(int(input()))

sum_cm = sum(cm)

for i in range(9):
    for j in range(i + 1, 9):
        if sum_cm - (cm[i] + cm[j]) == 100:
            result = [cm[k] for k in range(9) if k != i and k != j]
            result.sort()
            for i in result:
                print(i)
            exit()
