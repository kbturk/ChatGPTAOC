# Read the input data
grid = []
for i in range(5):
  row = input()
  grid.append([int(x) for x in row])

# Keep track of the number of visible trees
num_visible_trees = 0

# Iterate over each row and column of the grid
for i in range(5):
  for j in range(5):
    # Check if the tree at (i, j) is visible
    tree = grid[i][j]
    if tree == 0:
      # If the tree has height 0, it is not visible
      continue
    is_visible = True
    # Check if there are any other trees in the same row or column that are taller than this tree
    for k in range(5):
      if grid[i][k] > tree or grid[k][j] > tree:
        # If there is a taller tree in the same row or column, this tree is not visible
        is_visible = False
        break
    if is_visible:
      # If the tree is visible, increment the counter
      num_visible_trees += 1

# Print the total number of visible trees
print(num_visible_trees)

