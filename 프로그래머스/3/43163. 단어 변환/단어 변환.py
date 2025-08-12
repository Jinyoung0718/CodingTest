from collections import deque

def can_convert(word1, word2):
    diff = 0
    
    for a, b in zip(word1, word2):
        if a != b:
            diff += 1
            
            if diff > 1:
                return False
    
    return diff == 1 # 다른 게 하나일 때 True 반환

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin, 0)) # start 노드와 현재 횟수
    visited = set()
    
    while queue:
        cur_word, depth = queue.popleft()
        
        if cur_word == target:
            return depth
        
        for word in words:
            if word not in visited and can_convert(cur_word, word):
                visited.add(word)
                queue.append((word, depth + 1))