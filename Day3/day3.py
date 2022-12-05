#input = open(r"Day3\\test_day3.txt", "r")
input = open(r"Day3\\input_day3.txt", "r")
input = input.read().split('\n')
#input = [int(x) for x in input]

def get_priority(char: str):
    if char.islower():
       return(ord(char)-96)
    elif char.isupper():
        return(ord(char)-38)
    else:
        print("???")
        exit(1)

# Part 1
sum_of_prios = 0

for rucksack in input:
    if rucksack == '':
        continue
    first_comp, second_comp = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for item in first_comp:
        if item in second_comp:
            sum_of_prios += get_priority(item)
            break

# Part 2
group_list = zip(*(iter(input),) * 3)
sum_of_prios2 = 0

for group in group_list:
    shared_items = []
    for item in group[0]:
        if item in group[1]:
            shared_items.append(item)
    for item in shared_items:
        if item in group[2]:
            sum_of_prios2 += get_priority(item)
            break



print("Solution Part 1:")
print(f"The sum of priorities of wrongly sorted item types is {sum_of_prios}.")
print("Solution Part 2:")
print(f"The sum of priorities of badge item types is {sum_of_prios2}")