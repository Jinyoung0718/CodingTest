n, m = map(int, input().split())
k = int(input())
apple_loc = [int(input()) for _ in range(k)]


answer = 0
start = 1
end = m

for num in apple_loc:
    if start <= num <= end:
        continue
    elif num > end:
        distance = num - end
        start += distance
        end += distance
        answer += distance
    elif num < start:
        distance = start - num
        start -= distance
        end -= distance
        answer += distance

print(answer)