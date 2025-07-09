def solution(routes):
    routes.sort(key = lambda x: x[1])  # 진출 시점 기준 정렬
    
    camera_count = 0
    last_camera_position = -float('inf')  # 카메라 설치 안 된 초기값

    for route in routes:
        if route[0] > last_camera_position:
            camera_count += 1
            last_camera_position = route[1]

    return camera_count