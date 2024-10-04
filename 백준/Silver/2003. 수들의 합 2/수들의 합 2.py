n, m = map(int, input().split())
A = list(map(int, input().split()))

sum = A[0]
left = 0
right = 1
count = 0

while True:
    if sum < m:
        if right < n:
            sum += A[right]
            right += 1 # right를 먼저 더하면 끝 부분에서 오른쪽으로 이동 시, 인덱스 에러
        elif right >= n:
            break
    elif sum == m:
        count += 1
        sum -= A[left]
        left +=1 
    else:
        sum -= A[left]
        left += 1

print(count)

