#input = open(r"Day1\\test_day1.txt", "r")
input = open(r"Day1\\input_day1.txt", "r")
input = input.read().split('\n')
#input = [int(x) for x in input]

calories_sum = 0
calories_per_elf = []

for item in input:
    if item == '':
        calories_per_elf.append(calories_sum)
        calories_sum = 0
    else:
        calories_sum += int(item)
calories_per_elf.append(calories_sum)

calories_per_elf.sort()

print("Solution Part 1;")
print(f"The elf with the most calories has {max(calories_per_elf)} calories in his backpack.")
print("Solution Part 2:")
print(f"The top 3 elves with the most calories have {calories_per_elf[-1]+calories_per_elf[-2]+calories_per_elf[-3]} calories in total.")