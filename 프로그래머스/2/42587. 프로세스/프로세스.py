from collections import deque

def solution(priorities, location):
    
    queue = deque()
    answer = 0
    
    for idx, val in enumerate(priorities):
        queue.append([idx, val])
    
    while True:
        idx, val = queue.popleft()
        
        find = False
        
        for _, num in queue:
            
            if num > val:
                find = True
                break
        
        if find:
            queue.append((idx, val))
        else:
            answer += 1
            if idx == location:
                return answer