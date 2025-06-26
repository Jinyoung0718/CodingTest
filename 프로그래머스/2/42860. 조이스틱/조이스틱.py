def solution(name):
    answer = 0
    n = len(name)

    # 알파벳 변경 비용
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 커서 이동 최소 계산
    move = n - 1
    for i in range(n):
        next_i = i + 1
        # 연속된 A의 끝까지 찾기
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        # i에서 연속된 A를 건너뛰는 3가지 방향 비교
        distance = min(
            move,                         # 그냥 오른쪽 쭉 가기
            i * 2 + n - next_i,           # 왼쪽 갔다가 오른쪽 가기
            (n - next_i) * 2 + i          # 오른쪽 갔다가 왼쪽 가기
        )
        move = min(move, distance)

    return answer + move
