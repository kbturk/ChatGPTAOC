# Parse the input
heights = []
for line in open("input.txt"):
  heights.append(list(map(int, line.strip())))

# Count the number of visible trees in each row
row_visibility = []
for row in heights:
  max_height = max(row)
  count = 0
  for tree in row:
    if tree == max_height:
      count += 1
  row_visibility.append(count)

# Count the number of visible trees in each column
col_visibility = []
for col in zip(*heights):
  max_height = max(col)
  count = 0
  for tree in col:
    if tree == max_height:
      count += 1
  col_visibility.append(count)

# The total number of visible trees is the sum of
# the number of visible trees in each row and column
total_visibility = sum(row_visibility) + sum(col_visibility)

# Print the result
print(total_visibility)

