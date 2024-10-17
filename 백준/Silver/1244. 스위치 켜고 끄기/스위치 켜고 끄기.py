def change(index):
    if switch[index] == 1:
        switch[index] = 0
    else:
        switch[index] = 1

total = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    sex, target = map(int, input().split())

    if sex == 1:
        for i in range(target, len(switch), target):
            change(i)
    else:
        change(target)
        for i in range(total//2):
            if target + i > total or  target - i < 1: break # 범위는 항상 생각하자
            if switch[target + i] == switch[target - i]:
                change(target + i)
                change(target - i)
            else:
                break

for i in range(1, len(switch)):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()