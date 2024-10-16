dict = {1:31 ,2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for testcase in range(1, int(input()) + 1):
    result = 0

    month1, day1, month2, day2 = map(int, input().split())

    if month1 == month2:
        result = day2 - day1 + 1
    
    else:
        result = dict[month1] - day1

        for i in range(month1 + 1, month2):
            result += dict[i]
        
        result += day2 + 1 

    print(f"#{testcase} {result}")
