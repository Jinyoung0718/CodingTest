for testcase in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(2, n-2):
        left = max(arr[i - 1], arr[i -2])
        right = max(arr[i + 1], arr[i + 2])
        last = max(left, right)
        if arr[i] > last:
            result += arr[i] - last
        
    print(f'#{testcase} {result}')