for testcase in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    fee = [int(input()) for _ in range(n)]
    weight = [int(input()) for _ in range(m)]
    data = [int(input()) for _ in range(2*m)]
    
    parking = [0] * n
    waitng = []
    result = 0
    
    for i in data:
        if i < 0:
            index = parking.index(abs(i))
            if len(waitng) != 0:
                j = waitng.pop(0)
                parking[index] = j
                result += fee[index] * weight[j-1]
            else:
                parking[index] = 0
        else:
            if 0 not in parking:
                waitng.append(i)
            else:
                index = parking.index(0)
                parking[index] = i
                result += fee[index] * weight[i-1]

    print(f'#{testcase}', result)
