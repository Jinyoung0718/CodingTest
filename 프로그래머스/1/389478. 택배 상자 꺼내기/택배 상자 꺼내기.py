def solution(n, w, num):
    num_index = num - 1
    target_floor = num_index // w
    target_floor_pos = num_index % w
    count = 0
    
    target_col = target_floor_pos if target_floor % 2 == 0 else w - 1 - target_floor_pos
    
    floors = n // w
    if n % w != 0:
        floors += 1
    
    for i in range(target_floor, floors):
        start_num = (i * w) + 1
        end_num = min((i + 1) * w, n)  # 마지막 층은 박스가 꽉 안 찰 수 있음
        length = end_num - start_num + 1
        
        if i % 2 == 0:
            if target_col < length:
                count += 1
                
        else:
            if w - 1 - target_col < length:
                count += 1
    
    return count