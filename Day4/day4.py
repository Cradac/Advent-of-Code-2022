#input = open(r"Day4\\test_day4.txt", "r")
input = open(r"Day4\\input_day4.txt", "r")
input = input.read().split('\n')
input = [x.split(',') for x in input]

# Part 1

counter = 0
for pair in input:
    if '' in pair:
        continue
    first_lower, first_upper = pair[0].split('-')
    second_lower, second_upper = pair[1].split('-')
    if (int(first_lower) <= int(second_lower) and int(first_upper) >= int(second_upper)) or (int(first_lower) >= int(second_lower) and int(first_upper) <= int(second_upper)):
        counter += 1

# Part 2
counter2 = 0
for pair in input:
    if '' in pair:
        continue
    first_lower, first_upper = pair[0].split('-')
    second_lower, second_upper = pair[1].split('-')
    if int(first_lower) in range(int(second_lower),int(second_upper)) or int(first_upper) in range(int(second_lower),int(second_upper)) or int(second_lower) in range(int(first_lower),int(first_upper)) or int(second_upper) in range(int(first_lower),int(first_upper)):
        counter2 += 1
    elif int(first_lower) <= int(second_lower) and int(first_upper) >= int(second_upper) or int(first_lower) >= int(second_lower) and int(first_upper) <= int(second_upper):
        counter2 += 1


print("Solution Part 1:")
print(f"There are {counter} pairs that fully contain each other.")
print("Solution Part 2:")
print(f"There are {counter2} pairs that overlap at all.")