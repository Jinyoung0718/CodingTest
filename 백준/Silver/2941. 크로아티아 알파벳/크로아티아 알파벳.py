# 크로아티아 알파벳 리스트
memo = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
count = 0
i = 0

# 문자열 탐색
while i < len(word):
    matched = False
    for m in memo:
        # 현재 위치에서 크로아티아 알파벳 패턴과 일치하는지 확인
        if word[i:i+len(m)] == m:
            count += 1
            i += len(m)
            matched = True
            break
    if not matched:
        count += 1  # 일치하는 패턴이 없으면 일반 문자로 계산
        i += 1

print(count)
