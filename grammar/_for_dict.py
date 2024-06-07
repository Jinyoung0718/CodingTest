user_data = {"name":"진영", "age":20, "email" : "wo0982@naver.com"}

# for data in user_data:
#     print(data) # 키만 출력 된다
#     print(user_data[data]) # 이용하여 값을 찾는다
#     print(f"{data} : {user_data[data]}")

for data in user_data.items():
    print(data) # 튜플로 갖고안다
    print(f"{data[0]} : {data[1]}")
