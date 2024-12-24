word = input()

freq = {}
for char in word:
    freq[char] = freq.get(char, 0) + 1

mid = ''  # 중앙에 올 문자
flag = 0  # 홀수 개 문자 개수 카운트
for char in freq:
    if freq[char] % 2 == 1:
        mid = char
        flag += 1
        freq[char] -= 1
    if flag == 2:
        print("I'm Sorry Hansoo")
        exit()

# 팰린드_롬 구성
result = []  # 앞쪽 절반
for char in sorted(freq.keys()):  # 사전 순서로 정렬
    result.append(char * (freq[char] // 2))  # 짝수 개 문자 절반 추가

# 최종 팰린드_롬 생성
first_half = ''.join(result)
palindrome = first_half + mid + first_half[::-1]  # 중앙 문자와 뒷부분 추가
print(palindrome)