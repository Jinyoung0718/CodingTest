n, k = map(int, input().split())
number = list(map(int, input().split()))
cur_sum = sum(number[:k])
answer = [cur_sum]

for i in range(k, n):
    cur_sum = cur_sum - number[i-k] + number[i]
    answer.append(cur_sum)
print(max(answer))