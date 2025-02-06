while True:
    try:
        n = int(input())
    except:
        break

    num = 1
    count = 1

    while num % n != 0:
        num = num % n * 10 + 1  # 숫자 전체를 유지하지 않고 나머지만 활용
        count += 1

    print(count)
