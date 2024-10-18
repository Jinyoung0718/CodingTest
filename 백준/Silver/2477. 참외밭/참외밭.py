n = int(input())
width = []
height = []
total = []

for _ in range(6):
    dir, dist = map(int, input().split())

    if dir == 1 or dir == 2:
        width.append(dist)
    elif dir == 3 or dir == 4:
        height.append(dist)
    total.append(dist)

big_nemo = max(width) * max(height)

max_widht_idx = total.index(max(width))
max_height_idx = total.index(max(height))

small1 = abs(total[max_widht_idx - 1] - total[0 if max_widht_idx == 5 else max_widht_idx + 1])
small2 = abs(total[max_height_idx -1] - total[0 if max_height_idx == 5 else max_height_idx + 1])

result = big_nemo - (small1 * small2)
print(result * n)