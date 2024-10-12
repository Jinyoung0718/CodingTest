T = int(input())

for testcase in range(1, T + 1):
    n = int(input())
    data = list(map(int , input().split()))

    dict = {}

    for num in data:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    
    max_value = max(dict.values())
    result = [key for key, value in dict.items() if value == max_value]

    print(f"#{testcase}", *result)