import sys
input = sys.stdin.readline

n = int(input())
dic = {}
maxd = 0
data = list(int(input()) for _ in range(n))
data.sort()
print(round(sum(data) / n))
print(data[n//2])

for num in data:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
    
maxd = max(dic.values())
max_dic = []

for key in dic:
    if maxd == dic[key]:
        max_dic.append(key)

if len(max_dic) > 1:
    print(max_dic[1])
else:
    print(max_dic[0])

print(max(data) - min(data))