def solution(targets):
    # 끝점 오름차순 정렬
    targets.sort(key=lambda x: x[1])

    cnt = 0
    last = -float('inf')  # 마지막으로 찍은 'e' 값(실제로는 e - ε에 찍었다고 생각)

    for s, e in targets:
        # 개구간이라 s >= last면 기존 점(e - ε)은 이 구간에 포함되지 않음 → 새로 쏜다
        if s >= last:
            cnt += 1
            last = e  # 이번에는 e - ε에 쐈다고 생각하고 e만 기록

    return cnt
