n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

# 행 단위로 이동
def move(graph):
    for i in range(len(graph)):
        num = 0
        temp = []
        for n in graph[i]:
            if n == 0:
                continue
            elif n == num: 
                temp.append(num *2)
                num = 0
            else:
                if num == 0:
                    num = n
                elif num != 0:
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
    
    # 좌측 이동
    copy_graph = [lst[::] for lst in graph]
    move(copy_graph)
    dfs(copy_graph, count + 1)

    # 우측이동
    copy_graph = [lst[::-1] for lst in graph]
    move(copy_graph)
    dfs(copy_graph, count + 1)

    # 상방향
    graph_t = list(map(list, zip(*graph)))
    copy_graph = [lst[::] for lst in graph_t]
    move(copy_graph)
    dfs(copy_graph, count + 1)    

    # 하방향
    copy_graph = [lst[::-1] for lst in graph_t]
    move(copy_graph)
    dfs(copy_graph, count + 1)  

dfs(graph, 0)
print(result)