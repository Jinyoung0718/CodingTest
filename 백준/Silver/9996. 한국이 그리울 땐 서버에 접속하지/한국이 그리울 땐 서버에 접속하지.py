n = int(input())
pattern = input()

point = pattern.index("*")
prefix = pattern[:point]
suffix = pattern[point+1:]

result = []
for _ in range(n):
    word = input()
    if len(word) < len(prefix) + len(suffix):
        result.append("NE")
    elif word[:len(prefix)] == prefix and word[-len(suffix):] == suffix:
        result.append("DA")
    else:
        result.append("NE")

print("\n".join(map(str, result)))