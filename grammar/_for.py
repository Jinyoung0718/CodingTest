# days = ["월", "화", "수", "목", "금"]
#days = "월화수목금" <- 이것도 한 글자 씩 돌아가면서 iter을 하긴 한다

# for day in days:
#    print(f"{day}요일 입니다")

# print("종료")

# count = 1

# while count < 11:
#    print(f"{count}바퀴째")
#    count += 1

#print("달리기를 마쳤습니다")

num = 0

for i in range(1, 101): # 잎의 인덱스는 시작 지점, 뒷 인덱스는 범위
    print(f"{i}바퀴째")
    num += i
print("달리기를 마쳤습니다")
print(num)