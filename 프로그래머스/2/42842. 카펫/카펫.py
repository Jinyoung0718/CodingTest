def solution(brown, yellow):
    answer = []

    sum = brown + yellow

    for i in range(3,sum):
        col = i
        row = sum/i
        if sum%i == 0 :
            b = col + col + row + row - 4
            y = sum - b
            print(col,row,b,y)
            if brown == b and yellow == y :
                answer.append(row)
                answer.append(col)
                break

    return answer