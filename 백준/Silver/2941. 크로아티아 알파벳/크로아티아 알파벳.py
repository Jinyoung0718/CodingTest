# 크로아티아 알파벳 리스트
memo = ['dz=', 'lj', 'nj', 'c=', 'c-', 'd-', 's=', 'z=']

word = input()
count = 0
i = 0

# 문자열 탐색 (while 반복문 사용)
while i < len(word):
    for m in memo:
        if word[i:i+len(m)] == m:  # 현재 위치에서 패턴 일치 확인
            count += 1
            i += len(m)  # 패턴 길이만큼 건너뛰기
            break
    else:  # 어떤 패턴도 매칭되지 않은 경우
        count += 1
        i += 1  # 다음 문자로 이동

print(count)
