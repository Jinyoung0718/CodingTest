import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (N + 1)  # 인덱스 조정을 위해 크기를 N+1로 설정

# 부분합 계산
for i in range(1, N + 1):
    S[i] = S[i - 1] + A[i - 1]

# 쿼리 처리
for _ in range(M):
    a, b = map(int, input().split())
    print(S[b] - S[a - 1])
