dict = {"R": [1, 0], "L": [-1, 0], "B": [0, -1], "T": [0, 1], "RT": [1, 1], "LT": [-1, 1],
        "RB": [1, -1], "LB": [-1, -1]}
    
king, stone, n = input().split()

king_loc = list(map(int, [ord(king[0]) - 64, int(king[1])]))
stone_loc = list(map(int, [ord(stone[0]) - 64, int(stone[1])]))

for _ in range(int(n)):
    move = input()

    next_king_x = king_loc[0] + dict[move][0]
    next_king_y = king_loc[1] + dict[move][1]

    if 1 <= next_king_x <= 8 and 1 <= next_king_y <= 8:
        if stone_loc[0] == next_king_x and stone_loc[1] == next_king_y:
            next_stone_x = stone_loc[0] + dict[move][0]
            next_stone_y = stone_loc[1] + dict[move][1]
            if 1 <= next_stone_x <= 8 and 1 <= next_stone_y <= 8:
                king_loc = [next_king_x, next_king_y]
                stone_loc = [next_stone_x, next_stone_y]
        else:
            king_loc = [next_king_x, next_king_y]

print(chr(king_loc[0] + 64) + str(king_loc[1]))
print(chr(stone_loc[0] + 64) + str(stone_loc[1]))