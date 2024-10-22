def check():
    answer = 0

    for row in bingo:
        if row.count(0) == 5:
            answer += 1
    
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[j][i] == 0:
                cnt += 1
        if cnt == 5:
            answer += 1
    
    if all(bingo[i][i] == 0 for i in range(5)):
        answer += 1
    if all(bingo[i][4 - i] == 0 for i in range(5)):
        answer += 1

    return answer


bingo = [list(map(int, input().split())) for _ in range(5)]
mc = []

for i in range(5):
    mc += list(map(int, input().split()))

count = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if mc[i] == bingo[x][y]:
                bingo[x][y] = 0
                count += 1
    
    if count >= 12:
        result = check()
        if result >= 3:
            print(i + 1)
            break