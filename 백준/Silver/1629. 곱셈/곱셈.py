def mod_exp(a, b):
    if b == 1:  # 종료 조건: b가 1일 때
        return a % c

    # 재귀적으로 b를 절반으로 나눔
    result = mod_exp(a, b // 2)
    result = (result * result) % c  # 중간 결과에 mod 연산 적용

    if b % 2 == 1:  # b가 홀수라면 한 번 더 곱해줌
        result = (result * a) % c

    return result


# 입력
a, b, c = map(int, input().split())

# 출력
print(mod_exp(a, b))