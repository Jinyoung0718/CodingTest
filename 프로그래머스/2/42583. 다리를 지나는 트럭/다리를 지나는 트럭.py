from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    cur_weight = 0
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)
    
    while len(truck) > 0:
        time += 1
        cur_weight -= bridge.popleft() 
        # 이 동작은 1초가 흐를 때마다 트럭이 한 칸씩 앞으로 이동하는 것을 의미

        if cur_weight + truck[0] <= weight:
            cur_weight += truck[0]
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
        
    time += bridge_length
    return time