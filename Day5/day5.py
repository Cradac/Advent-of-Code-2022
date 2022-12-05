from copy import deepcopy

#input = open(r"Day5\\test_day5.txt", "r")
input = open(r"Day5\\input_day5.txt", "r")
input = input.read().split('\n')
#input = [x.split(',') for x in input]

index = 0
dirty_stacks = []

for line in input:
    index += 1
    if line == '':
        break
    # stack parsing
    line = [line[i:i+4] for i in range(0,len(line),4)]
    dirty_stacks.append(line)

dirty_stacks.reverse()
dirty_stacks.pop(0)

# creating final 2D list
stacks = [ [] for i in range(len(dirty_stacks[0])) ]

# cleaning up input & sorting into stacks
for line in dirty_stacks:
    line = [i.replace(' ', '') for i in line]
    line = [i.replace('[', '') for i in line]
    line = [i.replace(']', '') for i in line]
    
    col = 0
    for container in line:
        if container != '':
            stacks[col].append(container)
        col += 1

# split stack-image and instructions 
instructions = [i.split(' ') for i in input[index:]]
instructions.remove([''])

def exec_instructions(stacks, ins):
    for i in range(int(ins[1])):
        container = stacks[int(ins[3])-1].pop()
        stacks[int(ins[5])-1].append(container)
    return stacks

def exec_instructions_overhauled(stacks, ins):
    containers = []
    for i in range(int(ins[1])):
        container = stacks[int(ins[3])-1].pop()
        containers.append(container)
    containers.reverse()
    for container in containers:
        stacks[int(ins[5])-1].append(container)

    return stacks

def display_stacks(stacks):
    for col in stacks:
        print(col)

def get_solution(stacks):
    output = ''
    for col in stacks:
        if col != []:
            output += col[-1]
        else:
            output += ' '
    return output

stacks_overhauled = deepcopy(stacks)

for instruction in instructions:
    stacks = exec_instructions(stacks, instruction)

#print(stacks_overhauled)
for instruction in instructions:
    stacks_overhauled = exec_instructions_overhauled(stacks_overhauled, instruction)

print("Solution Part 1:")
print(f"Those are the top containers on each stack:")
print(get_solution(stacks))
print("Solution Part 2:")
print(f"Those are the top containers on each stack:")
print(get_solution(stacks_overhauled))
