move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
command_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S': 4, '^': 0, 'v': 1, '<': 2, '>': 3, 0: '^', 1: 'v', 2: '<', 3: '>'}

for testcase in range(1, int(input()) + 1):
    h, w = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    word_len = int(input())  
    commands = input()

    for i in range(h):
        for j in range(w):
            if graph[i][j] in ('<', '>', '^', 'v'):
                tank_loc = (i, j, command_dict[graph[i][j]])
                break

    for command in commands:
        temp = command_dict[command]
        if temp == 4:
            dy, dx = tank_loc[0], tank_loc[1]
            while True:
                dy += move_list[tank_loc[2]][0]
                dx += move_list[tank_loc[2]][1]
                if dy < 0 or dy >= h or dx < 0 or dx >= w or graph[dy][dx] == '#':
                    break
                if graph[dy][dx] == '*':
                    graph[dy][dx] = '.'
                    break

        else:
            y, x = tank_loc[0], tank_loc[1]
            graph[y][x] = command_dict[temp] 
            dy, dx = y + move_list[temp][0], x + move_list[temp][1]

            if 0 <= dy < h and 0 <= dx < w and graph[dy][dx] == '.':
                graph[y][x] = '.'  
                graph[dy][dx] = command_dict[temp] 
                tank_loc = (dy, dx, temp) 
            else:
                tank_loc = (y, x, temp)  
                
    print(f'#{testcase}', end = ' ')
    for row in graph:
        print(''.join(row))

