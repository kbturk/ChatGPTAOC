import sys
# Read the list of rucksacks from the input
ruck_lines = [line.strip() for line in sys.stdin]

# Initialize the sum of priorities to 0
total_prio = 0

# Loop over the groups of rucksacks
for i in range(0, len(ruck_lines), 3):
  # Get the three rucksacks in the current group
  ruck1, ruck2, ruck3 = ruck_lines[i:i+3]

  # Initialize the current priority to 0
  cur_prio = 0

  # Loop over the characters in the first rucksack
  for c in ruck1:
    # Check if the character appears in the other two rucksacks
    if c in ruck2 and c in ruck3:
      # If it does, update the current priority
      cur_prio = ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27

  # Add the current priority to the total
  total_prio += cur_prio

# Print the result
print(total_prio)
