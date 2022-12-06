# Initialize the stacks of characters
stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

# Parse the moves
moves = ['move 2 from 2 to 1']

for move in moves:
  # Split the move string into its component parts
  move_parts = move.split()

  # Parse the move quantity and the source and destination stacks
  move_qty = int(move_parts[1])
  src_stack = int(move_parts[3]) - 1
  dest_stack = int(move_parts[5]) - 1

  # Move the specified number of characters from the source stack to the destination stack,
  # in the correct order
  for i in range(move_qty):
    character = stacks[src_stack][-move_qty + i]
    stacks[src_stack].remove(character)
    stacks[dest_stack].append(character)

# Print the top characters of each stack
for stack in stacks:
  print(stack)
