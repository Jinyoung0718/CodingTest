def get_distance(dir, dist):
    if dir == 1:
        return dist
    elif dir == 2:
        return width + height + width - dist
    elif dir == 3:
        return (2 * width) + (2 * height) - dist
    else:
        return width + dist

width, height = map(int, input().split())
store = int(input())
store_path = []
result = []

for i in range(store + 1):
    if i == store:
        guard_direction, guard_dist = map(int, input().split())
    else:
        store_path.append(list(map(int, input().split())))

guard_path = get_distance(guard_direction, guard_dist)

for store_dir, store_dist in store_path:
    store_dist = get_distance(store_dir, store_dist)

    clock_path = abs(guard_path - store_dist)
    counter_clock_path = (2 * width) + (2 * height) - clock_path

    result.append(min(clock_path, counter_clock_path))

print(sum(result))