n = int(input())
graph = [list(input()) for _ in range(n)]

def quety(y, x, size):
    if size == 1:
        return graph[y][x]

    check = graph[y][x]
    result = ""
    
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] != check:
                result += '('
                result += quety(y, x, size // 2)
                result += quety(y, x + (size // 2), size // 2)
                result += quety(y + (size // 2), x, size // 2)
                result += quety(y + (size // 2), x + (size // 2), size // 2)
                result += ')'
                return result
    return check

print(quety(0, 0, n))