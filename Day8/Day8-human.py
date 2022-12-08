from copy import deepcopy
import sys
from typing import List, Tuple, Set

def what_a_view(tree: Tuple[int,int], grid: List[List[int]]) -> int:
    score = 1
    tree_height = grid[tree[0]][tree[1]]
    tree_count = 0

    if 0 in tree:
        return 0

    #tree to right:
    for i in range(tree[1]+1,len(grid[0]),1):
        tree_count +=1
        if tree_height <= grid[tree[0]][i]:
            break

    score *= max(tree_count,1)
    tree_count = 0

    #tree to left:
    for i in range(tree[1]-1,-1,-1):
        tree_count +=1
        if tree_height <= grid[tree[0]][i]:
            break

    score *= max(tree_count,1)
    tree_count = 0

    #slide up this time:
    for i in range(tree[0]-1,-1,-1):
        tree_count +=1
        if tree_height <= grid[i][tree[1]]:
            break

    score *= max(tree_count,1)
    tree_count = 0

    #slide down this time:
    for i in range(tree[0]+1,len(grid),1):
        tree_count +=1
        if tree_height <= grid[i][tree[1]]:
            break

    score *= max(tree_count,1)
    tree_count = 0

    #dance real smooth
    return score

def count_trees(grid: List[List[int]], visible_trees: Set[Tuple[int,int]]) -> Set[Tuple[int,int]]:
    #left to right
    #x = # of rows
    max_height = -1
    for x in range(0,len(grid)):
        #y = # of columns
        for y in range(0,len(grid[0])):
            #the max tree height is 9, so if we've seen a max height, go to the next row
            if grid[x][y] > max_height:
                #if the tree is taller than every tree seen so far, add it to the visible tree list
                visible_trees.add((x,y))
                max_height = grid[x][y]
        max_height = -1

    #top to bottom
    max_height = -1
    for y in range(0,len(grid)):
        #y = # of columns
        for x in range(0,len(grid[0])):
            if grid[x][y] > max_height:
                #if the tree is taller than every tree seen so far, add it to the visible tree list
                visible_trees.add((x,y))
                max_height = grid[x][y]
        max_height = -1

    #right to left
    max_height = -1
    for x in range(len(grid)-1,-1,-1):
        #y = # of columns
        for y in range(len(grid[0])-1,-1,-1):
            if grid[x][y] > max_height:
                #if the tree is taller than every tree seen so far, add it to the visible tree list
                visible_trees.add((x,y))
                max_height = grid[x][y]
        max_height = -1

    #bottom to top
    max_height = -1
    for y in range(len(grid)-1,-1,-1):
        #y = # of columns
        for x in range(len(grid[0])-1,-1,-1):
            #the max tree height is 9, so if we've seen a max height, go to the next row
            if grid[x][y] > max_height:
                #if the tree is taller than every tree seen so far, add it to the visible tree list
                visible_trees.add((x,y))
                max_height = grid[x][y]
        max_height = -1

    return visible_trees

def main():
    grid = [list(map(int,line.strip('\n'))) for line in sys.stdin]

    #trees that are visible from the edge of the map
    visible_trees: Set[Tuple[int,int]] = set()

    visible_trees = count_trees(grid, visible_trees)
    print(len(visible_trees))
    print(max([what_a_view((i,j), grid) for i in range(len(grid)) for j in range(len(grid[0]))]))
    return 1

if __name__ == '__main__':
    sys.exit(main())
