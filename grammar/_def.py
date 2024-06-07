def add(a, b):
    print(f"{a}와 {b}를 입력받았습니다")
    print(f"두 값을 더하면 {a+b} 입니다")
    return a+b

temp = add(5, 10)

add(temp, 100)

print(f"합은 {temp}")