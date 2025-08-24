def solution(points, routes):
    answer = 0
    robot_pos = {i + 1: tuple(points[i]) for i in range(len(points))}
    count = {}
    
    for route in routes:
        time = 0
        x, y = robot_pos[route[0]]
        count[(time, x, y)] = count.get((time, x, y), 0) + 1
        
        for target_node in route[1:]:
            tx, ty = robot_pos[target_node]
            dir_x = tx - x
            dir_y = ty - y
            
            next_x = -1 if dir_x < 0 else 1
            for _ in range(abs(dir_x)):
                x += next_x
                time += 1
                count[(time, x, y)] = count.get((time, x, y), 0) + 1
            
            next_y = -1 if dir_y < 0 else 1
            for _ in range(abs(dir_y)):
                y += next_y
                time += 1
                count[(time, x, y)] = count.get((time, x, y), 0) + 1
    
    for val in count.values():
        if val >= 2:
            answer += 1
    
    return answer