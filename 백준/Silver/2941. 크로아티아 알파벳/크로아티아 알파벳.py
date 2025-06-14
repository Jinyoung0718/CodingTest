croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

sentence = input()
idx = 0

for word in croatia:
    sentence = sentence.replace(word, "*")

print(len(sentence))