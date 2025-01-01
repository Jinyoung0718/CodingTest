n = int(input())
a = [list(input()) for _ in range(n)]


# 쿼드 트리 함수 정의
def quard(y, x, size):
    if size == 1:
        return a[y][x]  # 기저 조건: 사이즈가 1일 때 해당 문자를 반환

    b = a[y][x]  # 첫 번째 문자를 기준으로 설정
    result = ""

    # 전체 영역이 같은 문자(0 또는 1)인지 확인
    for i in range(y, y + size):
        for j in range(x, x + size):
            if a[i][j] != b:  # 다른 문자가 발견되면 4등분
                result += '('
                result += quard(y, x, size // 2)  # 왼쪽 위
                result += quard(y, x + size // 2, size // 2)  # 오른쪽 위
                result += quard(y + size // 2, x, size // 2)  # 왼쪽 아래
                result += quard(y + size // 2, x + size // 2, size // 2)  # 오른쪽 아래
                result += ')'
                return result

    # 모든 문자가 동일하면 해당 문자 반환
    return b


# 결과 출력
print(quard(0, 0, n))
