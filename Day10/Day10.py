# Parse the program
program = [line.strip() for line in open('program.txt')]

# Initialize the X register to 1
X = 1

# Initialize the cycle number to 0
cycle = 0

# Initialize the signal strength at each point in time to 0
signal_strength = [0, 0, 0, 0, 0, 0]

# Execute the program
while cycle < len(program):
  # Increment the cycle number
  cycle += 1
  
  # Get the current instruction
  instruction = program[cycle - 1]
  
  # If the instruction is "addx", increment the X register by the specified value
  if instruction.startswith('addx'):
    X += int(instruction.split()[1])
  
  # If the current cycle is the 20th, 60th, 100th, 140th, 180th, or 220th cycle,
  # update the signal strength at that point in time
  if cycle in [20, 60, 100, 140, 180, 220]:
    signal_strength[cycle // 40] = cycle * X

# Print the signal strength at each point in time
print(sum(signal_strength))
