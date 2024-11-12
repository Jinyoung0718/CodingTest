n = int(input())
graph = [[0] * n for _ in range(n)]
result = 0
v1 = [0] * (n +  1)
v2 = [0] * (2 * (n + 1))
v3 = [0] * (2 * (n + 1))

def dfs(depth):
    global result

    if depth == n:
        result += 1
        return
    
    for i in range(n):
        if v1[i] == v2[depth + i] == v3[depth - i] == 0:
            v1[i] = v2[depth + i] = v3[depth - i] = 1
            dfs(depth + 1)
            v1[i] = v2[depth + i] = v3[depth - i] = 0


dfs(0)
print(result)