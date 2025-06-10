word = input()
answer = []
temp = ""
in_tag = False

for n in word:

    if n == "<":
        answer.append(temp[::-1])
        answer.append("<")
        temp = ""
        in_tag = True

    elif n == ">":
        answer.append(">")
        in_tag = False

    elif in_tag:
        answer.append(n)

    elif n == " ":
        answer.append(temp[::-1])
        answer.append(" ")
        temp = ""

    else:
        temp += n

if temp:
    answer.append(temp[::-1])

print("".join(answer))
