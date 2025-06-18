n, k = map(int, input().split())
medals = []

for _ in range(n):
    country, gold, silver, bronze = map(int, input().split())
    medals.append([country, gold, silver, bronze])

# 메달 수 기준 정렬 (금, 은, 동 내림차순)
medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1  # 현재 등수
same = 1  # 동점자 수
prev = medals[0][1:]  # 이전 메달 수
rank_dict = {medals[0][0]: rank}  # 국가번호: 등수 저장

for i in range(1, n):
    cur = medals[i][1:]
    if cur == prev:
        # 메달이 같으면 등수도 같음
        rank_dict[medals[i][0]] = rank
        same += 1
    else:
        # 메달이 다르면 현재 등수 = 이전 등수 + 동점자 수
        rank += same
        rank_dict[medals[i][0]] = rank
        same = 1
        prev = cur

print(rank_dict[k])
