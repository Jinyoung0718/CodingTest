import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * n
C = [0] * m # 나머지, 나머지 값은 0부터 m -1 까지 가능하므로 길이가 m인 배열을 사용한다

S[0] = A[0]
result = 0

for i in range(1, n):
	S[i] = S[i-1] + A[i] # 합 배열 저장


for i in range(n):
	remainder = S[i] % m # 합 배열의 모든 값에 % 연산 수행
	if remainder == 0:   # 0 ~ i 까지의 구간 합 자체가 0일 때 정답에 더하기
		result += 1
	
	C[remainder] += 1

for i in range(m):
	# 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
	if C[i] > 1:
		result += (C[i] * (C[i]-1) // 2)
	
print(result)