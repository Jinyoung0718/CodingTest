for testcase in range(1, int(input()) + 1):
    data = list(map(int, input().split()))

    result = []
    max_data = max(data)
    min_data = min(data)

    for num in data:
        if num != max_data and num != min_data:
            result.append(num)

    if len(result) > 0:
        answer = round(sum(result) / len(result))
    else:
        answer = 0

    print(f"#{testcase} {answer}")