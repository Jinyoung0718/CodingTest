n = int(input())

# 입력받은 문자열을 리스트 형태로 저장
graph = [input() for _ in range(n)]

# 첫 번째 문자열을 기준으로 설정
ret = list(graph[0])

# 각 문자열을 순회하며 조건에 맞는 처리를 수행
for i in range(1, n):
    for j in range(len(graph[0])):
        if graph[i][j] != ret[j]:
            ret[j] = '?'  # 리스트로 변경된 문자열의 값을 수정

# 최종 결과를 문자열로 변환하여 출력
result = ''.join(ret)
print(result)
