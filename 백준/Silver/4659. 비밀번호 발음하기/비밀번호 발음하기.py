def is_acceptable(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    has_vowel = False  # 1번 조건: 모음이 하나 라도 있는지 확인
    consecutive_vowel = 0  # 2번 조건: 연속된 '모음' 개수
    consecutive_consonant = 0  # 2번 조건: 연속된 '자음' 개수

    prev_char = ''  # 3번 조건: 연속된 같은 문자 체크

    for char in word:
        if char in vowels:
            has_vowel = True
            consecutive_vowel += 1
            consecutive_consonant = 0  # 자음 연속 개수 초기화
        else:
            consecutive_consonant += 1
            consecutive_vowel = 0  # 모음 연속 개수 초기화

        # 2. 모음/자음이 3개 연속이면 불가능한 비밀번호
        if consecutive_vowel >= 3 or consecutive_consonant >= 3:
            return False

        # 3. 같은 글자가 연속으로 두 번 오는지 체크 (ee, oo는 허용)
        if prev_char == char and char not in {'e', 'o'}:
            return False
        
        prev_char = char
        
    return has_vowel  # 모음이 하나라도 있어야 True 반환

while True:
    word = input().strip()
    if word == 'end':
        break
    if is_acceptable(word):
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')
