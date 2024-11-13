def solution(n, stations, w):
    result = 0
    effect = 2 * w + 1
    current_position = 1
    dist = []

    for i in stations:
        left_border = i - w
        if left_border - current_position > 0:
            gap = left_border - current_position
            result += gap // effect
            if gap % effect != 0:
                result += 1

        current_position = i + w + 1

    if current_position <= n:
        gap = n - current_position + 1
        result += gap // effect
        if gap % effect != 0:
            result += 1
            
    return result