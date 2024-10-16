for testcase in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    sdoku = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if sdoku[i][j] == 1:
                count += 1
            else:
                if count == m:
                    result += 1
                count = 0
        if count == m:
            result += 1
    
    for i in range(n):
        count = 0
        for j in range(n):
            if sdoku[j][i] == 1:
                count += 1
            else:
                if count == m:
                    result += 1
                count = 0
        if count == m:
            result += 1 
    
    print(f"#{testcase} {result}")