n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

def move(graph):
    for i in range(len(graph)):
        temp = []
        num = 0
        for n in graph[i]:
            if n == 0: continue
            elif num != n:
                if num == 0:
                    num = n
                elif num != 0:
                    temp.append(num)
                    num = n
            elif num == n:
                temp.append(num * 2)
                num = 0
        
        if num != 0:
            temp.append(num)
        
        graph[i] = temp + ([0] * (len(graph[i]) - len(temp)))

def dfs(depth, graph):
    global result

    if depth == 5:
        result = max(result, max(map(max, graph)))
        return
    

    copy_graph = [row[::] for row in graph]
    move(copy_graph)
    dfs(depth + 1, copy_graph)

    copy_graph = [row[::-1] for row in graph]
    move(copy_graph)
    dfs(depth + 1, copy_graph)

    copy_graph_t = list(map(list, zip(*graph)))
    copy_graph = [row[::] for row in copy_graph_t]
    move(copy_graph)
    dfs(depth + 1, copy_graph)

    copy_graph = [row[::-1] for row in copy_graph_t]
    move(copy_graph)
    dfs(depth + 1, copy_graph)

dfs(0, graph)
print(result)