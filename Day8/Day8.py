# Parse the input
heights = []
for line in open("input.txt"):
  heights.append(list(map(int, line.strip())))

# Count the number of visible trees in each row
row_visibility = []
for row in heights:
  count = 0
  max_height = -1
  for tree in row:
    if tree > max_height:
      count += 1
      max_height = tree
  row_visibility.append(count)

# Count the number of visible trees in each column
col_visibility = []
for col in zip(*heights):
  count = 0
  max_height = -1
  for tree in col:
    if tree > max_height:
      count += 1
      max_height = tree
  col_visibility.append(count)

# Count the number of visible trees in each row (reversed)
rev_row_visibility = []
for row in heights:
  count = 0
  max_height = -1
  for tree in reversed(row):
    if tree > max_height:
      count += 1
      max_height = tree
  rev_row_visibility.append(count)

# Count the number of visible trees in each column (reversed)
rev_col_visibility = []
for col in zip(*heights):
  count = 0
  max_height = -1
  for tree in reversed(col):
    if tree > max_height:
      count += 1
      max_height = tree
  rev_col_visibility.append(count)

# The total number of visible trees is the sum of
# the number of visible trees in each row and column
total_visibility = sum(row_visibility) + sum(col_visibility) + sum(rev_row_visibility) + sum(rev_col_visibility)

# Print the result
print(total_visibility)

