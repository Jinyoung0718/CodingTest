counting = [0] * 26

string = str(input())

for s in string:
    counting[ord(s) - ord('a')] += 1


print(" ".join(map(str, counting)))