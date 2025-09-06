def solution(elements):
    n = len(elements)
    sums = set()
    elements *= 2
    prefix = [0]
    
    for num in elements:
        prefix.append(prefix[-1] + num)
    
    for length in range(1, n + 1):
        for start in range(n):
            end = length + start
            temp = prefix[end] - prefix[start]
            sums.add(temp)
    
    return len(sums)