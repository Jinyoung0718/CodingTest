result = 0
A = list(map(str, input().split("-")))

def mySum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        result += temp
    else:
        result -= temp

print(result)