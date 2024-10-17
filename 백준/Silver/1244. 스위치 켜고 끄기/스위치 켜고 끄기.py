def change(index):
    if switch[index] == 1:
        switch[index] = 0
    else:
        switch[index] = 1

n = int(input())
switch = [-1] + list(map(int, input().split()))
total = int(input())

for _ in range(total):
    sex, target = map(int, input().split())
    
    if sex == 1:
        for i in range(target, n + 1, target):
            change(i)
    
    else:
        change(target)
        for k in range(n//2):
            if target - k < 1 or target + k > n: break
            if switch[target + k] == switch[target - k]:
                change(target + k)
                change(target - k)
            else:
                break

for i in range(1, n + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()