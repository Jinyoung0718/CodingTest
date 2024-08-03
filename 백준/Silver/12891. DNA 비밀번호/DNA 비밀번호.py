checkList = [0] * 4  # 비밀번호 체크 리스트
myList = [0] * 4  # 현재 상태 리스트
checkSecret = 0  # 몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수

def myadd(c):  # 새로 들어온 문자를 처리하는 함수
    global checkList, myList, checkSecret

    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):
    global checkList, myList, checkSecret

    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
result = 0
A = list(input().strip())
checkList = list(map(int, input().split()))

# 초기 설정에서 0인 문자에 대해 checkSecret 증가
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

# 처음 P 길이의 윈도우에 대해 설정
for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    result += 1

# 슬라이딩 윈도우 적용
for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        result += 1

print(result)