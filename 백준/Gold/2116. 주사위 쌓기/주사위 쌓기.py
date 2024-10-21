N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
rotate = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0} 
maxd = 0

for i in range(6):
    result = []
    temp = [1, 2, 3, 4, 5, 6]
    temp.remove(dice[0][i])  # 아랫면을 랜덤으로 고름 각 랜덤 값마다의 최대값을 구하려 함
    next = dice[0][rotate[i]]  # 랜덤으로 골라진 아랫면의 대응하는 윗면의 값을 저장하고 지움
    temp.remove(next) 
    result.append(max(temp))

    for j in range(1, N): 
        temp = [1, 2, 3, 4, 5, 6]
        temp.remove(next) # 윗면의 값은 두 번째 주사위 부터는 아랫면에 해당하므로 지운다
        next = dice[j][rotate[dice[j].index(next)]] #  
        temp.remove(next) 
        result.append(max(temp))
    
    result = sum(result) 
    if maxd < result: 
        maxd = result

print(maxd)

# 주사위를 쌓을 때마다 각 주사위의 옆면 중 가장 큰 숫자를 합산하여 최댓값을 구하는 문제입니다.