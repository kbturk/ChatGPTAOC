input = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"

# Split the input into individual pairs
pairs = input.split(",")

# Create a list of ranges
ranges = []
for pair in pairs:
    # Split each pair into two numbers
    numbers = pair.split("-")
    # Convert the numbers to integers and create a range
    r = range(int(numbers[0]), int(numbers[1]) + 1)
    # Add the range to our list of ranges
    ranges.append(r)

# Keep track of the number of overlaps
overlaps = 0

# Iterate over the ranges
for r1 in ranges:
    for r2 in ranges:
        # Check if the ranges have a common element
        if r1 != r2 and any(i in r1 for i in r2):
            # If they do, then increment the overlap count
            overlaps += 1

# Print the number of overlaps
print(overlaps)

