A, B, C = map(int, input().split())
temp = [0] * 100

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        temp[i] += 1

time_1 = temp.count(1)
time_2 = temp.count(2)
time_3 = temp.count(3)

print((time_1 * A) + ((time_2 * B) * 2) + ((time_3 * C) * 3))