def solution(sizes):    
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        larger = max(w, h)
        smaller = min(w, h)
        
        max_w = max(max_w, larger)
        max_h = max(max_h, smaller)
        
    return max_w * max_h