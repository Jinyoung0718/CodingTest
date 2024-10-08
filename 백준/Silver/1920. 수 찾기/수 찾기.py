n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
target_list = list(map(int ,input().split()))

for i in range(m):
    target = target_list[i]
    start = 0
    end = len(A) - 1
    find = False

    while start <= end:
        mid_index = int((start + end) // 2)
        mid_value = A[mid_index]

        if mid_value > target:
            end = mid_index - 1
        elif mid_value < target:
            start = mid_index + 1
        else:
            find = True
            break

    if find:
        print(1)
    else: 
        print(0)