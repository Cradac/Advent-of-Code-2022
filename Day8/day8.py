#input = open(r"Day8\\test_day8.txt", "r")
input = open(r"Day8\\input_day8.txt", "r")
input = input.read().split('\n')
#input = [x for x in input]

# grid[0] = y
# grid[1] = x
grid = []
global sc_scores 
sc_scores = []

for y in input:
    if y == '':
        continue
    row = []
    grid.append(row)
    for x in y:
        row.append(int(x))

def check_visibility(position: list, grid: list, size: int) -> bool:
    up_flag, down_flag, left_flag, right_flag = True, True, True, True
    up_score, down_score, left_score, right_score = 0,0,0,0

    # edge check
    if position[0] == 0 or position[0] == len(grid[0])-1 or position[1] == 0 or position[1] == len(grid)-1:
        return True
    # check up

    for i in reversed(range(0,position[0])):
        if grid[i][position[1]] >= size and up_flag:
            up_flag = False
            up_score += 1
        elif up_flag:
            up_score += 1
    # check down
    for i in range(position[0]+1,len(grid)):
        if grid[i][position[1]] >= size and down_flag:
            down_flag = False
            down_score += 1
        elif down_flag:
            down_score += 1
    # left check
    for i in reversed(range(0,position[1])):
        if grid[position[0]][i] >= size and left_flag:
            left_flag = False
            left_score += 1
        elif left_flag:
            left_score += 1
    # right check
    for i in range(position[1]+1,len(grid[0])):
        if grid[position[0]][i] >= size and right_flag:
            right_flag = False
            right_score += 1
        elif right_flag:
            right_score += 1

    #print(up_score,down_score,left_score,right_score)
    sc_scores.append(up_score*down_score*left_score*right_score)
    return up_flag or down_flag or left_flag or right_flag
    
visibility_counter = 0

for y in range(len(grid)):
    y_row = grid[y]
    for x in range(len(y_row)):
        if check_visibility([y,x], grid, grid[y][x]):
            visibility_counter +=1 



print("Solution Part 1:")
print(f"There are {visibility_counter} visible trees in this grid.")
print("Solution Part 2:")
print(f"The highest scenic score is {max(sc_scores)}.")