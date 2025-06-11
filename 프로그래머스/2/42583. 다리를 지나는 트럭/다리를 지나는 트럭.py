from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    cur_weight = 0
    answer = 0
    
    while bridge:
        answer += 1
        n = bridge.popleft()
        cur_weight -= n
        
        if truck_weights:
            if cur_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                cur_weight += truck
            else:
                bridge.append(0)
    
    return answer