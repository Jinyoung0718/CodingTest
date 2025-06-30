from collections import deque

def solution(people, limit):
    
    people.sort()
    queue = deque(people)
    answer = 0
    
    while queue:
        
        if len(queue) >= 2 and queue[0] + queue[-1] <= limit:
            queue.popleft()
        
        queue.pop()
        answer += 1
    
    return answer