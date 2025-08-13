import re

def solution(new_id):
    # 1단계: 소문자로 변환
    new_id = new_id.lower()
    
    # 2단계: 허용 문자만 남기기 (a-z, 0-9, -, _, .)
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    
    # 3단계: 마침표 2번 이상 → 1개로
    new_id = re.sub(r'\.+', '.', new_id)
    
    # 4단계: 처음과 끝의 마침표 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열이면 'a' 대입
    if new_id == '':
        new_id = 'a'
    
    # 6단계: 길이 16 이상이면 15자까지만 남김, 끝 마침표 제거
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    
    # 7단계: 길이 2 이하라면 마지막 문자를 3이 될 때까지 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
