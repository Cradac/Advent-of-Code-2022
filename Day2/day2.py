#input = open(r"Day2\\test_day2.txt", "r")
input = open(r"Day2\\input_day2.txt", "r")
input = input.read().split('\n')
#input = [int(x) for x in input]

# X = Rock, Y = Paper, Z = Scissors
player_map = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

win_points = 6
draw_points = 3
loss_points = 0

def rps(input: str):
    points = 0
    opponent, player = input.split(' ')
    # draw
    if opponent=='A' and player=='X' or opponent=='B' and player=='Y' or opponent=='C' and player=='Z':
        points += draw_points
    # player win
    elif opponent=='A' and player=='Y' or opponent=='B' and player=='Z' or opponent=='C' and player=='X':
        points += win_points
    # player loss
    elif opponent=='A' and player=='Z' or opponent=='B' and player=='X' or opponent=='C' and player=='Y':
        points += loss_points
    points += player_map[player]
    return points

# Part 2

'''
 index for strtegy guide: ABC / Rock,Paper,Scissorstranslates to index 012
 outter layer is your strategy, inner layer is opponents play
 output is a key for player_map

'''
strategy_guide = {
    # win strategy
    'Z': ['Y', 'Z', 'X'],
    # draw strategy
    'Y': ['X', 'Y', 'Z'],
    # loss strategy
    'X': ['Z', 'X', 'Y']
}

# A = Rock, B = Paper, C = Scissors
# maps opponents play to index in strategy_guide
opponent_map = {
    'A': 0,
    'B': 1,
    'C': 2
}

strategy_points = {
    'X': 0,
    'Y': 3,
    'Z': 6 
}

def rps_overhauled(input: str):
    opponent, strategy = input.split(' ')
    points = strategy_points[strategy]
    player_key = strategy_guide[strategy][opponent_map[opponent]]
    points += player_map[player_key]
    return points

point_total_1 = 0
for game in input:
    point_total_1 += rps(game)

point_total_2 = 0
for game in input:
    point_total_2 += rps_overhauled(game)

print("Solution Part 1:")
print(f"If you play after the strategy guide your point total is {point_total_1}")
print("Solution Part 2:")
print(f"If you play after the strategy guide your point total is {point_total_2}")
