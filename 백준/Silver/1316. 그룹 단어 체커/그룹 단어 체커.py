n = int(input())  # 단어의 개수 입력
group_word_count = 0  # 그룹 단어의 개수를 세는 변수

# 각 단어를 검사
for _ in range(n):
    word = input()  # 단어 입력
    is_group_word = True  # 그룹 단어인지 여부를 나타내는 변수
    seen = set()  # 등장한 문자를 저장할 집합
    previous_char = ''  # 이전 문자를 저장할 변수

    for char in word:
        if char != previous_char:
            if char in seen:  # 이미 등장한 문자가 다시 등장하면 그룹 단어가 아님
                is_group_word = False
                break
            seen.add(char)  # 처음 등장하는 문자를 집합에 추가
        previous_char = char  # 이전 문자를 현재 문자로 업데이트

    if is_group_word:
        group_word_count += 1  # 그룹 단어이면 카운트 증가

# 결과 출력
print(group_word_count)
