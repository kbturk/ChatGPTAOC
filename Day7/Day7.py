# The maximum directory size
MAX_SIZE = 100000

# The total size of the current directory
current_dir_size = 0

# The overall sum of the sizes of the directories with a total size of at most MAX_SIZE
overall_sum = 0

# The current directory
current_dir = "/"

# A dictionary that maps directories to their total sizes
dir_sizes = {}

# The list of commands and output
commands = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]

# Process the commands and output
for line in commands:
    # Check if this is a command
    if line.startswith("$"):
        # Split the command into parts
        parts = line.split()

        # Get the command and its argument
        cmd = parts[1]
        arg = parts[2] if len(parts) > 2 else None

        # Handle the "cd" command
        if cmd == "cd":
            # Update the current directory size if the current directory
            # is being changed to a child directory
            if arg != "/" and arg in dir_sizes:
                current_dir_size += dir_sizes[arg]

            # Reset the current directory size if the current directory
            # is being changed to the outermost directory
            elif arg == "/":
                current_dir_size = 0

            # Change the current directory
            current_dir = arg

    # Otherwise, this is output from the "ls" command
    else:
        # Split the output into parts
        parts = line.split()

        # Get the type of the entry and its name
        entry_type = parts[0]
        name = parts[1]

        # Handle a file
        if entry_type != "dir":
            # Update the current directory size
            current_dir_size += int(parts[0])

        # Handle a directory
        else:
            # Update the current directory size if the directory has
            # not been encountered before
            if name not in dir_sizes:
                dir_sizes[name] = current_dir_size

            # Add the current directory's size to the overall sum
            # Add the current directory's size to the overall sum
            # if its size is at most MAX_SIZE
            if current_dir_size <= MAX_SIZE:
                overall_sum += current_dir_size

# Print the overall sum
print(overall_sum)

