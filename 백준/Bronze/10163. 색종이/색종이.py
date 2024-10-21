grid = [[0] * 1001 for _ in range(1001)]
num_of_papers = int(input())

for paper_id in range(1, num_of_papers + 1):
    start_x, start_y, width, height = map(int, input().split())
    
    # 색종이의 범위를 평면에 표시
    for y in range(start_y, start_y + height):
        grid[y][start_x:start_x + width] = [paper_id] * width

for paper_id in range(1, num_of_papers + 1):
    visible_area = 0
    for row in range(1001):
        visible_area += grid[row].count(paper_id)

    print(visible_area)
