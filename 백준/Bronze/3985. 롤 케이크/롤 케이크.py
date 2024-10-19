# 입력 처리
L = int(input())  # 롤 케이크의 길이
N = int(input())  # 방청객의 수

requests = []
expected_pieces = [0] * (N + 1)
actual_pieces = [0] * (N + 1)
cake = [0] * (L + 1)  # 케이크 조각 초기화, 0으로 설정

# 방청객이 요청한 범위 저장
for i in range(1, N + 1):
    P, K = map(int, input().split())
    requests.append((P, K))
    expected_pieces[i] = K - P + 1

# 가장 많은 조각을 받을 것으로 기대한 방청객 찾기
most_expected_index = expected_pieces.index(max(expected_pieces[1:]))

# 실제로 조각을 받은 방청객 처리
for idx, (P, K) in enumerate(requests, start=1):
    for j in range(P, K + 1):
        if cake[j] == 0:  # 아직 아무도 차지하지 않은 조각이라면
            cake[j] = idx
            actual_pieces[idx] += 1

# 실제로 가장 많은 조각을 받은 방청객 찾기
most_actual_index = actual_pieces.index(max(actual_pieces[1:]))

# 결과 출력
print(most_expected_index)
print(most_actual_index)
