#input = open(r"Day9\\test_day9.txt", "r")
#input = open(r"Day9\\test2_day9.txt", "r")
input = open(r"Day9\\input_day9.txt", "r")
input = input.read().split('\n')
input = [x.split(' ') for x in input]

visited_by_tail = [(0,0)]
visited_by_longer_tail = [(0,0)]

direction_map = {
    'U': (0,1),
    'D': (0,-1),
    'R': (1,0),
    'L': (-1,0)
}

# rope[0] = head
# rope[-1] = tail
rope = [(0,0),(0,0)]
longer_rope = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

def step(direction: str, rope: list, tail_list: list):
    # move head
    rope[0] = rope[0][0]+direction[0],rope[0][1]+direction[1]

    # move other parts
    for i in range(1,len(rope)):
        previous_segment = rope[i-1]
        difference = previous_segment[0]-rope[i][0],previous_segment[1]-rope[i][1]
        pull_force = [0,0]
        if abs(difference[0]) > 1 or abs(difference[1]) > 1:
            # move in the direction
            # x move
            if difference[0] != 0:
                pull_force[0] = 1 if difference[0] > 0 else -1
            # y move
            if difference[1] != 0:
                pull_force[1] = 1 if difference[1] > 0 else -1
        rope[i] = rope[i][0]+pull_force[0],rope[i][1]+pull_force[1]


    # solution, simulation & return
    tail_list.append(rope[-1])
    #simulate(rope, tail_list)
    return rope, tail_list

# simulation is kinda borked and limited. Only works correctly on the first test set
def simulate(rope: list, tail_list):
    # y
    for y in reversed(range(6)):
        new_line = ''
        # x
        for x in range(5):
            if (x,y) in rope:
                new_line+= str(rope.index((x,y))) if rope.index((x,y)) != 0 else 'H'
            elif (x,y) == (0,0):
                new_line+='s'
            elif (x,y) in tail_list:
                new_line+='#'
            else:
                new_line+='.'
        print(new_line)
    print('')

##print('== Initial State ==')
##print('')
##simulate(rope)

# Part 1

for line in input:
    if line[0] == '':
        continue
    for i in range(int(line[1])):
        rope, visited_by_tail = step(direction_map[line[0]], rope, visited_by_tail)


# Part 2
for line in input:
    if line[0] == '':
        continue
    for i in range(int(line[1])):
        rope, visited_by_longer_tail = step(direction_map[line[0]], longer_rope, visited_by_longer_tail)



print("Solution Part 1:")
print(f"The tail of the rope has visited {len(set(visited_by_tail))} positions.")
print("Solution Part 2:")
print(f"The tail of the rope has visited {len(set(visited_by_longer_tail))} positions.")