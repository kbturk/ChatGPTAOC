# Parse the program
program = [line.strip() for line in open('program.txt')]

# Initialize the X register to 1
X = 1

# Initialize the cycle number to 0
cycle = 0

# Execute the program
while cycle < len(program):
  # Increment the cycle number
  cycle += 1
  
  # Get the current instruction
  instruction = program[cycle - 1]
  
  # If the instruction is "addx", increment the X register by the specified value
  if instruction.startswith('addx'):
    X += int(instruction.split()[1])

# Compute the signal strength of the CPU
signal_strength = cycle * X

# Print the signal strength
print(signal_strength)
