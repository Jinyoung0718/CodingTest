n = int(input())
data = list(map(int, input().split()))
count = 1
max_length = 1

for i in range(1, n):
    if data[i] <= data[i-1]:
        count += 1
    else:
        count = 1
    
    if count > max_length:
        max_length = count

count = 1

for i in range(1, n):
    if data[i] >= data[i-1]:
        count += 1
    else:
        count = 1
    
    if count > max_length:
        max_length = count

print(max_length)