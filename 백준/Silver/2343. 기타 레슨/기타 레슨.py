n, m = map(int, input().split())
lesson = list(map(int, input().split()))

start = 0
end = 0

for i in lesson:
    if start < i:  # 레슨 최대값을 시작 인덱스로 저장
        start = i 
    end += i        # 모든 레슨의 총합을 종료 인덱스로 저장

while start <= end:
    middle = int((start + end) // 2)
    sum = 0 # 각 블루레이에 들어가는 레슨 길이 합
    count = 0 # 블루레이의 개수

    for i in range(n): # 중간값으로 모든 레슨을 저장할 수 있는지 확인
        if sum + lesson[i] > middle:
            # 현재 블루레이에 저장할 수 없어 새로운 블루레이로 교체
            count += 1 # 더이상 못담으르므로 새로운 블루레이 추가
            sum = 0
        sum += lesson[i]
    
    if sum != 0: # 총합계가 0으로 딱 떨어지지 않으면 블루레이가 하나 더 필요
        count += 1

    if count > m: # 중간 인덱스값으로 모든 레슨 저장 불가능
        start = middle + 1 # 블루레이 크기를 늘려야 합니다. 그래서 start를 middle + 1로 설정
    else:         # 중간 인덱스값으로 모든 레슨 저장 가능
        end = middle - 1 # 블루레이 크기를 줄일 수 있으므로 end를 middle - 1로 설정

print(start)