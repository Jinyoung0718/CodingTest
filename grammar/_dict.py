user = {"name" : "진영", "job" : "프로그래머", "email" : "wo0982@naver.com"}

#{키 : 값} 값으로 숫자나 리스트도 가능

# print(user["name"]) # 인덱스로는 불가하다

user["age"] = 15 # 추가 가능

# print(user)

del user["name"] # 삭제 가능

# print(user)

user["age"] = 25 # 덮어 씌워진다

# print(user)

# keys_list = user.keys() # keys 메소드로 딕셔너리 키 값을 모음이 가능
# keys_list = list(keys_list) # 리스트로 변경 가능

# value_list = user.values() # 벨류도 모음이 가능하다
# value_list = list(value_list) # 리스트로 변경 가능

# 리스트 변경 이유는 append, insert, count, 등등의 기능을 사용하기 위함이다

# item_list = user.items() 키와 값 둘 다 가져와서 튜플 형식으로 출력한다 

