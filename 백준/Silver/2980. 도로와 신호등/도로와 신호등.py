n, l = map(int, input().split())
time = 0
current_position = 0

for _ in range(n):
    d, r, g = map(int, input().split())  # 신호등 위치, 빨간불 시간, 초록불 시간
    time += d - current_position  # 신호등 위치까지 이동하는 시간 추가
    current_position = d

    # 현재 시간이 신호등의 빨간불인 경우
    cycle_time = time % (r + g)
    if cycle_time < r:
        time += r - cycle_time  # 빨간불이 끝날 때까지 기다린다

# 마지막 신호등에서 끝까지 이동
time += l - current_position
print(time)
