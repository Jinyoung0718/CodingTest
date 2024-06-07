food = [100, "햄버거", "감자튀김", "김치", "삼겹살"]
# 서로 다른 타입이여도 리스트 구성 가능

food2 = [100,["햄버거", "감자튀김"],"김치", "삼겹살"]

food3 = food + food2
food4 = food * 3 # 곱한 것이 나옴
food.append("피자")
food.insert(0, "피자") # 어디에 추가할 지 인덱스 번호 추가 가능
food.remove("김치") # 맨 첫 김치만 삭제
print(food.count("김치"))
print(food.index("감자튀김"))

print(food)
print(food2[1]) # ["햄버거", "감자튀김"]
print(food2[1][0]) # "햄버거"
print(food3) # [100, '햄버거', '감자튀김', '김치', '삼겹살', 100, ['햄버거', '감자튀김'], '김치', '삼겹살']

example = ["C", "A", "B"]
# example.sort(reverse=True) 
# print(example)

example[0] = "알파벳 싫어"
print(example)