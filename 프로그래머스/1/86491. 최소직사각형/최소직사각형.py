def solution(sizes):
    max_width = 0
    max_height = 0

    for w, h in sizes:
        larger = max(w, h)
        smaller = min(w, h)

        max_width  = max(max_width, larger)
        max_height = max(max_height, smaller)

    return max_width * max_height