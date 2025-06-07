def solution(arguments):
    queue = list()
    for operation in arguments :
        if operation[0] == 'I' :
            queue.append(int(operation[1 : ]))
        elif operation[0] == 'D' :

            if len(queue) == 0 :
                continue

            if int(operation[1 : ]) == 1 :
                queue.remove(max(queue))
            elif int(operation[1 : ]) == -1 :
                queue.remove(min(queue))

    if len(queue) == 0 :
        answer = [0, 0]
    else :
        answer = [max(queue), min(queue)]

    return answer