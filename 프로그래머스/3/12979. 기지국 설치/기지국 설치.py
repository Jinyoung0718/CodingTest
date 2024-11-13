def solution(n, stations, w):
    answer = 0
    coverage = w * 2 + 1  # 한 기지국이 커버할 수 있는 아파트 범위
    current_position = 1  # 현재 전파가 닿지 않는 시작 위치

    for station in stations:
        # 현재 기지국의 도달 범위 이전에 전파가 닿지 않는 구간이 있을 경우
        left_bound = station - w  # 현재 기지국의 왼쪽 끝 범위
        if left_bound > current_position:
            gap_length = left_bound - current_position  # 전파가 닿지 않는 구간 길이
            answer += gap_length // coverage  # 필요한 기지국 개수 추가
            if gap_length % coverage > 0:  # 남은 구간이 있을 경우
                answer += 1
        # 현재 기지국이 도달할 수 있는 범위의 다음 위치로 갱신
        current_position = station + w + 1

    # 마지막 기지국 이후로 전파가 닿지 않는 구간 처리
    if current_position <= n:
        gap_length = n - current_position + 1
        answer += gap_length // coverage
        if gap_length % coverage > 0:
            answer += 1

    return answer