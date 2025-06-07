import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())  # N: 수의 개수, L: 윈도우 크기
A = list(map(int, input().split()))  

window = deque() 

for i in range(N):
    while window and window[-1][0] > A[i]:
        window.pop()

    window.append((A[i], i))
    if window[0][1] <= i - L:
        window.popleft()
    print(window[0][0], end=" ")
print()