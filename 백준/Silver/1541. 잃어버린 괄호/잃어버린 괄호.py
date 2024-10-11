data = list(map(str, input().split("-")))
result = 0

def mySum(num):
    temp = sum(map(int, num.split("+")))
    return temp

for i in range(len(data)):
    temp = mySum(data[i])
    if i == 0:
        result += temp
    else:
        result -= temp

print(result)