import sys
sys.setrecursionlimit(10000)

n = int(input())  # N자리 수

# 소수 판별 함수
def is_Prime(num):
    if num == 1:  # 1은 소수가 아님
        return False
    for i in range(2, int(num**(1/2)) + 1):  # 2부터 제곱근까지 확인
        if num % i == 0:
            return False
    return True

# DFS 탐색 함수
def dfs(number, length):
    if length == n:  # N자리 숫자가 완성되면 출력
        print(number)
        return
    for i in range(1, 10, 2):  # 다음 자리에 홀수만 가능 (짝수는 소수가 아님)
        new_number = number * 10 + i
        if is_Prime(new_number):  # 새로운 숫자가 소수이면 계속 탐색
            dfs(new_number, length + 1)

# 한 자리 소수로 시작 (2, 3, 5, 7)
dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)
