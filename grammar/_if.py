today = 15

if today < 30:
    print("아직 돈이 없네...")
elif today == 30:
    print("돈 들어오는 날~")    
else:
    print("무슨 요일이지?")

# pizza = " " 빈칸도 무언가가 존재하기에 True 취급 "" <- 이 경우는 False

pizza = True
hamburger = True

if pizza and hamburger:
    print("야호 피자다")
elif pizza or hamburger:
    print("와! 햄버거당~")
elif not pizza:
    print("피자가 아니다")
else:
    print("아 배고파")