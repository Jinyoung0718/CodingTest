n, k = map(int, input().split())
data = list(range(1, n+1))
reuslt = []
index = 0
while data:

    index = (k + index - 1) % len(data)
    reuslt.append(data.pop(index))

print("<" + ", ".join(map(str, reuslt)) + ">")