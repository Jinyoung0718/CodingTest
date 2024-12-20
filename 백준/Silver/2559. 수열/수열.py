n, k = map(int, input().split())
data = list(map(int, input().split()))

current_sum = sum(data[:k])
max_sum = current_sum

for i in range(k, n):
    current_sum = current_sum - data[i - k] + data[i]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)