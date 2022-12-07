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
print(ranges)

# Count the number of pairs where one range fully contains the other
count = 0
for i in range(len(ranges)):
  for j in range(i+1, len(ranges)):
    if ranges[i][0] <= ranges[j][0] and ranges[i][1] >= ranges[j][1]:
      count += 1
    elif ranges[j][0] <= ranges[i][0] and ranges[j][1] >= ranges[i][1]:
      count += 1

# Print the result
print(count)

