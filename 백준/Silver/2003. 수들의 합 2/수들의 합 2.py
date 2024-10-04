su, target = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 0
count = 0
sum = 0

while True:
    if sum < target:
        if right < su:
            sum += A[right]
            right += 1
        else:
            break
    elif sum > target:
        sum -= A[left]
        left += 1
    else:
        count += 1
        sum -= A[left]
        left += 1 

print(count)