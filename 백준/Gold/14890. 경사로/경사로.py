n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

def check(row, visited):
    count = 1
    for i in range(1, len(row)):
        if row[i-1] == row[i]:
            count += 1
        elif row[i-1] + 1 == row[i] and count >= l and visited[i-l:i] == [False] * l:
            count = 1
            visited[i-l:i] = [True] * l
        elif row[i-1] > row[i]:
            count = 1
        else:
            return False
    
    return True

for _ in range(2):
    for row in graph:
        visited = [False] * len(row)
        if check(row, visited) and check(row[::-1], visited[::-1]):
            result += 1
        
    graph = list(map(list, zip(*graph)))

print(result)