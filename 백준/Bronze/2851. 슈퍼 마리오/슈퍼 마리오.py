scores = [int(input()) for _ in range(10)]

sum_score = 0
answer = 0

for score in scores:
    sum_score += score

    if abs(100 - sum_score) < abs(100 - answer):
        answer = sum_score
    elif abs(100 - sum_score) == abs(100 - answer):
        answer = max(answer, sum_score)

print(answer)