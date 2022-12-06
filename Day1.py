#part1
calories = []
elf_calories = []

# Read input
while True:
    try:
        line = input()
        if line == '':
            calories.append(elf_calories)
            elf_calories = []
        else:
            elf_calories.append(int(line))
    except EOFError:
        break

# Find the elf with the most calories
most_calories = 0
for elf_calorie_list in calories:
    if sum(elf_calorie_list) > most_calories:
        most_calories = sum(elf_calorie_list)

print(most_calories)

#part2
calories = []
elf_calories = []

# Read input
while True:
    try:
        line = input()
        if line == '':
            calories.append(elf_calories)
            elf_calories = []
        else:
            elf_calories.append(int(line))
    except EOFError:
        break

# Sort the elves by the number of calories they are carrying
calories.sort(key=sum, reverse=True)

# Calculate the sum of the top three elves
top_three_calories = sum(calories[0]) + sum(calories[1]) + sum(calories[2])

print(top_three_calories)
