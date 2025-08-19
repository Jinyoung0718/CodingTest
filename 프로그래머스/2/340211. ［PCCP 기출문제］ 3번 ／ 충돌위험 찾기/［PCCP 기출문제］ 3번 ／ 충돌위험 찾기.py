def solution(points, routes):
    answer = 0
    
    # 1) 포인트 번호 -> 좌표 매핑(1-indexed 번호)
    coord = {i+1: tuple(points[i]) for i in range(len(points))}

    # 2) (time, r, c) 별 로봇 수 카운트
    cnt = {}

    # 3) 각 로봇에 대해 시뮬레이션 (t=0에서 첫 포인트에 있음)
    for route in routes:
        r, c = coord[route[0]]
        t = 0
        cnt[(t, r, c)] = cnt.get((t, r, c), 0) + 1

        for nxt in route[1:]:
            nr, nc = coord[nxt]
            dr = nr - r     # r축 방향으로 몇 칸 이동해야 하는지(차이)
            dc = nc - c     # c축 방향으로 몇 칸 이동해야 하는지(차이)

            # r축 먼저 이동
            # dr이 음수면 현재 좌표에서 위로, 양수면 아래로 이동한다
            step_r = 1 if dr > 0 else -1
            for _ in range(abs(dr)):
                r += step_r
                t += 1
                cnt[(t, r, c)] = cnt.get((t, r, c), 0) + 1

            # c축 이동
            # dc이 음수면 현재 좌표에서 오른쪽으로, 양수면 왼쪽으로 이동한다
            step_c = 1 if dc > 0 else -1
            for _ in range(abs(dc)):
                c += step_c
                t += 1
                cnt[(t, r, c)] = cnt.get((t, r, c), 0) + 1
        # 마지막 포인트에 도착한 순간까지만 기록

    # 4) 위험 상황 집계
    for v in cnt.values():
        if v >= 2:
            answer += 1
            
            
    return answer