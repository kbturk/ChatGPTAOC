import sys

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

# Solve problem 1
if len(sys.argv) < 2 or sys.argv[1] == '1':
    # Find the elf with the most calories
    most_calories = 0
    for elf_calorie_list in calories:
        if sum(elf_calorie_list) > most_calories:
            most_calories = sum(elf_calorie_list)

    print(most_calories)

# Solve problem 2
elif sys.argv[1] == '2':
    # Calculate the sum of the top three elves
    if len(calories) >= 3:
        top_three_calories = sum(calories[0]) + sum(calories[1]) + sum(calories[2])
    else:
        top_three_calories = 0

    print(top_three_calories)

# Invalid argument
else:
    print('Invalid argument')
