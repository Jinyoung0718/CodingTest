dict = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

king, stone, n = input().split()
n = int(n)

king_loc = list(map(int, [ord(king[0]) - 64, int(king[1])]))
stone_loc = list(map(int, [ord(stone[0]) - 64, int(stone[1])]))

for _ in range(n):
    move = input()

    next_king_locX = king_loc[0] + dict[move][0]
    next_king_locY = king_loc[1] + dict[move][1]

    if 1 <= next_king_locX <= 8 and 1 <= next_king_locY <= 8:
        if stone_loc[0] == next_king_locX and stone_loc[1] == next_king_locY:
            next_stone_locX = stone_loc[0] + dict[move][0]
            next_stone_locY = stone_loc[1] + dict[move][1]
            if 1 <= next_stone_locX <= 8 and 1 <= next_stone_locY <= 8:
                king_loc = [next_king_locX, next_king_locY]
                stone_loc = [next_stone_locX, next_stone_locY]
        else:
            king_loc = [next_king_locX, next_king_locY]
    
print(chr(king_loc[0] + 64) + str(king_loc[1]))
print(chr(stone_loc[0] + 64) + str(stone_loc[1]))