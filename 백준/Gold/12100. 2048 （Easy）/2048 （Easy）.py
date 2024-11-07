n = int(input())
graph_origin = [list(map(int, input().split())) for _ in range(n)]
result = 0

def move(graph):
    for i in range(len(graph)):
        num = 0
        temp = []
        for n in graph[i]:
            if n == 0:
                continue
            elif n == num: 
                temp.append(num * 2)
                num = 0
            else:
                if num != 0:
                    temp.append(num)
                num = n
        if num != 0:
            temp.append(num)
        graph[i] = temp + [0] * (len(graph[i]) - len(temp))

def dfs(graph, count):
    global result

    if count == 5:
        result = max(result, max(map(max, graph)))
        return

    left_graph = [row[::] for row in graph]
    move(left_graph)
    dfs(left_graph, count + 1)

    right_graph = [row[::-1] for row in graph]
    move(right_graph)
    dfs(right_graph, count + 1)

    graph_transe = list(map(list, zip(*graph)))

    up_graph = [row[::] for row in graph_transe]
    move(up_graph)
    dfs(up_graph, count + 1)    

    down_graph = [row[::-1] for row in graph_transe]
    move(down_graph)
    dfs(down_graph, count + 1)

dfs(graph_origin, 0)
print(result)
