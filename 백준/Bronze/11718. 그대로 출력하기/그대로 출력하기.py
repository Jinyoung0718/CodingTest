lis = []

try:
    while True:
        n = input()

        if n == "":  
            break

        lis.append(n)

except EOFError: 
    pass

for i in lis:
    print(i)
