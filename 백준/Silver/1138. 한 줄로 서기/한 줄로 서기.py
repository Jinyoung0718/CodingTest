import sys

n = int(sys.stdin.readline())

# 자신보다 왼쪽에 있는 키 큰 사람의 수
people = list(map(int, sys.stdin.readline().split()))

# 키 순서대로 사람들을 나열
height = [0] * n

for i in range(n):
    # 자신의 왼쪽에 있는 키 큰 사람의 수
    cnt = 0
    for j in range(n):

        # 자신의 왼쪽에 있는 키 큰 사람의 수와 맞고, 그 자리에 아무도 없다면
        if cnt == people[i] and height[j] == 0:
            height[j] = i + 1
            break

        # 자리에 아무도 없다면 자신의 왼쪽에 키 큰 사람의 수를 카운트
        elif height[j] == 0:
            cnt += 1

print(*height)