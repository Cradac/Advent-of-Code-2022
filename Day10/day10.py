#input = open(r"Day10\\test_day10.txt", "r")
input = open(r"Day10\\input_day10.txt", "r")
input = input.read().split('\n')
input = [x.split(' ') for x in input]

register_X = 1
cycle_number = 0
signal_strengths = {}

def increment_cycle(cycle_number: int, register_X: int, signal_strengths):
    # execution during cycle
    draw((register_X-1,register_X,register_X+1),cycle_number)
    # cycle incrementation
    cycle_number +=1
    # excution after cycle
    if cycle_number in [20,60,100,140,180,220]:
        get_signal_strength(cycle_number, register_X)
    # part 2
    if cycle_number%40 == 0:
        print('')
        
    #print(cycle_number, register_X)
    return cycle_number, register_X, signal_strengths

def get_signal_strength(cycle_number: int, register_X: int):
    signal_strengths[cycle_number] = register_X
    return cycle_number * register_X

def addx(register_X: int, V: int):
    return register_X + V

def noop():
    return

def draw(sprite_pos: list, cycle_number: int):
    #print(cycle_number, end=' ')
    if cycle_number%40 in sprite_pos:
       print('█', end='')
       	#█
    else:
       print(' ', end='')


for i in range(len(input)):
    instruction = input[i]
    if instruction[0] == '':
        continue
    if instruction[0] == 'noop':
        cycle_number, register_X, signal_strengths = increment_cycle(cycle_number, register_X, signal_strengths)
        noop()
    if instruction[0] == 'addx':
        cycle_number, register_X, signal_strengths = increment_cycle(cycle_number, register_X, signal_strengths)
        cycle_number, register_X, signal_strengths = increment_cycle(cycle_number, register_X, signal_strengths)
        register_X = addx(register_X, int(instruction[1]))



    


print('')
for cycle_number, register_X in signal_strengths.items():
    print(f'Signal strength in cycle {cycle_number}: {cycle_number*register_X}')


print("Solution Part 1:")
print(f"The sum of all signal strengths is {sum(x*y for x,y in signal_strengths.items())}.")
print("Solution Part 2:")
print(f"")