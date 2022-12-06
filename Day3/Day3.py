import sys
# Read the list of rucksacks from the input
ruck_lines = [line.strip() for line in sys.stdin]

# Initialize the sum of priorities to 0
total_prio = 0

# Loop over the rucksacks
for ruck in ruck_lines:
  # Split the rucksack into its two compartments
  comp1, comp2 = ruck[:len(ruck)//2], ruck[len(ruck)//2:]

  # Initialize the current priority to 0
  cur_prio = 0

  # Loop over the characters in the first compartment
  for c in comp1:
    # Check if the character appears in the second compartment
    if c in comp2:
      # If it does, update the current priority
      cur_prio = ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27

  # Add the current priority to the total
  total_prio += cur_prio

# Print the result
print(total_prio)
