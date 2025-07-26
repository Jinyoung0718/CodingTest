from collections import deque

def bfs(start, target):
    visited = [False] * 10000
    queue = deque()
    queue.append((start, ""))  # (현재 숫자, 명령어 문자열)
    visited[start] = True

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path

        # D: n을 두 배로 바꿈, 결과과 9999 보다 큰 경우 10000 으로 나눈 나머지를 취함
        d = (current * 2) % 10000 # ex) 2 % 4 = 2 : 앞 숫자가 높으면 그대로 반환
        if not visited[d]:
            visited[d] = True
            queue.append((d, path + "D"))

        # S: n에서 1을 뺀 결과 n-1을 레지스터에 저장, n이 0 이라면 9999가 저장
        s = current - 1 if current != 0 else 9999
        if not visited[s]:
            visited[s] = True
            queue.append((s, path + "S"))

        # L: 네 자릿수는 왼편부터 d2, d3, d4, d1 로 회전한다 (각 자릿수를 왼편 회전)
        l = (current % 1000) * 10 + (current // 1000)
        if not visited[l]:
            visited[l] = True
            queue.append((l, path + "L"))

        # R:네 자릿수는 왼편부터 d4, d1, d2, d3 로 회전한다 (각 자릿수를 오른쪽 회전)
        r = (current % 10) * 1000 + (current // 10)
        if not visited[r]:
            visited[r] = True
            queue.append((r, path + "R"))

testcase = int(input())
for _ in range(testcase):
    A, B = map(int, input().split())
    print(bfs(A, B))