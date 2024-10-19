def get_distance(direction, distance):
    if direction == 1:
        return distance
    elif direction == 2:
        return width + height + width - distance
    elif direction == 3:
        return (2 * width) + (2 * height) - distance 
    else:
        return width + distance

width, height = map(int, input().split())
store = int(input())
store_position = []

for i in range(store + 1):
    if i == store:
        guard_dir, guard_dist = map(int, input().split())
    else:
        store_position.append(list(map(int, input().split())))
    
total_dist = 0
guard_path = get_distance(guard_dir, guard_dist)

for direction, distance in store_position:
    store_path = get_distance(direction, distance)

    clockwise_dist = abs(guard_path - store_path)
    counter_clockwise_dict = (2 * width) + (2 * height) - clockwise_dist

    total_dist += min(clockwise_dist, counter_clockwise_dict)

print(total_dist)