def solution(n, w, num):
    # 박스 인덱스를 0부터 시작
    num_index = num - 1
    floor = num_index // w   # 해당 박스의 층 (0층이 맨 아래)
    pos_in_floor = num_index % w  # 층에서의 위치

    # 해당 층의 방향에 따라 실제 열 번호 계산
    if floor % 2 == 0:  # 왼→오
        col = pos_in_floor
    else:               # 오→왼
        col = w - 1 - pos_in_floor

    count = 0
    # 해당 층부터 위로 올라가면서 같은 열의 박스 개수 세기
    for f in range(floor, (n + w - 1) // w):  # 마지막 층까지
        start_num = f * w + 1
        end_num = min((f + 1) * w, n)
        length = end_num - start_num + 1

        if f % 2 == 0:  # 왼→오
            if col < length:
                count += 1
        else:           # 오→왼
            if w - 1 - col < length:
                count += 1

    return count
