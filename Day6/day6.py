#input = open(r"Day6\\test_day6.txt", "r")
input = open(r"Day6\\input_day6.txt", "r")
input = input.read().split('\n')
#input = [x.split(',') for x in input]

def is_duplicate(list: list):
    if len(list) != len(set(list)):
        return True
    else:
        return False

def detect_sop_marker(sequence: str):
    marker_stack = []
    index = 0
    for char in sequence:
        index += 1
        if char not in marker_stack and len(marker_stack) == 3 and not is_duplicate(marker_stack):
            return index
        marker_stack.append(char)
        if len(marker_stack) > 3:
            marker_stack.pop(0)

def detect_som_marker(sequence: str):
    marker_stack = []
    index = 0
    for char in sequence:
        index += 1
        if char not in marker_stack and len(marker_stack) == 13 and not is_duplicate(marker_stack):
            return index
        marker_stack.append(char)
        if len(marker_stack) > 13:
            marker_stack.pop(0)

for sequence in input:
    if sequence == '':
        continue
    solution1 = detect_sop_marker(sequence)
    solution2 = detect_som_marker(sequence)
    print(solution1, solution2)


print("Solution Part 1:")
print(f"The first start-of-packet marker is detected after processing {solution1} characters.")
print("Solution Part 2:")
print(f"The first start-of-message marker is detected after processing {solution2} characters.")
