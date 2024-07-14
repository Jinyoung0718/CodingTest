from collections import Counter

def solution(strArr):
    
    lis = [len(item) for item in strArr]
    cnt = Counter(lis)
    return max(cnt.values())