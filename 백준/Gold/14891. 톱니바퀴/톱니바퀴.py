n = 4
graph = [[0] * 8] + [list(map(int, input())) for _ in range(n)]
k = int(input())
top = [0] * (n + 1)
result = 0

for _ in range(k):
    target, direction = map(int, input().split())
    temp = [(target, 0)]

    for i in range(target + 1, n+1):
        if graph[i-1][(top[i-1] + 2) % 8] != graph[i][(top[i] + 6) % 8]:
            temp.append((i, (i - target) % 2))
        else:
            break
    
    for i in range(target-1, 0, -1):
        if graph[i+1][(top[i+1] + 6) % 8] != graph[i][(top[i] + 2) % 8]:
            temp.append((i, (target - i) % 2))
        else:
            break
    
    
    for index, rotate in temp:
        if rotate == 0:
            top[index] = (top[index] - direction + 8) % 8
        else:
            top[index] = (top[index] + direction + 8) % 8

cal_list = [0, 1, 2, 4, 8]

for i in range(1, n+1):
    result += graph[i][top[i]] * cal_list[i]

print(result)