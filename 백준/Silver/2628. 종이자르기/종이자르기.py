r, c = map(int, input().split())

r_arr = [0, r]
c_arr = [0, c]

result_x = []
result_y = []

for i in range(int(input())):
    choice, line = map(int, input().split())

    if choice == 1:
        r_arr.append(line)
    else:
        c_arr.append(line)

r_arr.sort()
c_arr.sort()

for i in range(len(r_arr) - 1):
    result_x.append(r_arr[i + 1] - r_arr[i])

for i in range(len(c_arr) - 1):
    result_y.append(c_arr[i + 1] - c_arr[i])

print(max(result_x) * max(result_y))