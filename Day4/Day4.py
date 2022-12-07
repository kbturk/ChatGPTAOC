# Read in the input
pairs = []
while True:
  try:
    line = input()
  except EOFError:
    break
  pairs.append(line)

# Parse the pairs into ranges
ranges = []
for pair in pairs:
  for range_str in pair.split(','):
    ranges.append(list(map(int, range_str.split('-'))))

# Count the number of pairs where one range fully contains the other
count = 0
for i in range(0, len(ranges), 2):
  if ranges[i][0] <= ranges[i+1][0] and ranges[i][1] >= ranges[i+1][1]:
    count += 1
  elif ranges[i+1][0] <= ranges[i][0] and ranges[i+1][1] >= ranges[i][1]:
    count += 1

# Print the result
print(count)

