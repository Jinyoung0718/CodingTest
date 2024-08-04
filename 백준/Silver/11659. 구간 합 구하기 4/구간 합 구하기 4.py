import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (n + 1)

S[0] = A[0]

for i in range(1, n+1):
    S[i] = S[i-1] + A[i - 1]


for _ in range(m):
    s, e = map(int, input().split())
    print(S[e] - S[s-1])