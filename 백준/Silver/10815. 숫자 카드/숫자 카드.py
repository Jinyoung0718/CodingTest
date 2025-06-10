n = int(input())
my_card = list(map(int, input().split()))

m = int(input())
your_card = list(map(int, input().split()))

answer = []
memo = {}

for card in my_card:
    memo[card] = memo.get(card, 0) + 1

for card in your_card:
    if card in memo:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)