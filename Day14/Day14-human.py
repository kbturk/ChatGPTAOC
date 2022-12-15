import sys, queue, json
from typing import Optional, Tuple, TypeAlias, List, Set
from functools import cmp_to_key

Rock: TypeAlias = Tuple[int,int]
Sand: TypeAlias = Tuple[int,int]

def build_cave(edges: List[Tuple[int,...]]) -> Set[Rock]:
    rock_wall: Set[Rock] = set()
    for i in range(len(edges)-1):
        if edges[i][0] - edges[i+1][0] <=0:
            xstart, xend = edges[i][0], edges[i+1][0]
        else:
            xstart, xend = edges[i+1][0], edges[i][0]

        if edges[i][1] - edges[i+1][1] <=0:
            ystart, yend = edges[i][1], edges[i+1][1]
        else:
            ystart, yend = edges[i+1][1], edges[i][1]
        rock_wall.update(set([(x,y) for x in range(xstart, xend+1) for y in range(ystart, yend+1)]))
        #print(f'added: {rock_wall} ')
    return rock_wall

def fill_cave2(sand_start, cave: Set[Rock]) -> int:
    sand: Set[Sand] = set([sand_start])
    len_last_sand = 0

    floor =  max([y for _,y in cave.union(sand)]) + 2

    while True:
        falling_sand = sand_start
        falling = True

        #if we didn't add any sand then the simulation is complete
        if len(sand) == len_last_sand:
            break
        else:
            len_last_sand = len(sand)
            #print(f'last sand: {len_last_sand}')

        while falling:

            #try going straight down
            peek = (falling_sand[0],falling_sand[1] + 1)
            if peek[1] >= floor:
                falling = False

            check = peek[1] < floor
            #print(peek)
            if peek not in cave and peek not in sand and check:
                falling_sand = peek

            #try going down and left
            elif (peek[0] - 1, peek[1]) not in cave and (peek[0] - 1, peek[1]) not in sand and check:
                falling_sand = (peek[0] - 1, peek[1])

            #try going down and right
            elif (peek[0] + 1, peek[1]) not in cave and (peek[0] + 1, peek[1]) not in sand and check:
                falling_sand = (peek[0] + 1, peek[1])

            #can't move anymore. Sand comes to a rest
            else:
                sand.add(falling_sand)
                falling = False

    print(len(sand))

    return 1

def fill_cave(sand_start, cave: Set[Rock]) -> int:
    sand: Set[Sand] = set()
    len_last_sand = len(sand)

    floor =  max([y for _,y in cave.union(sand)]) 

    while True:
        falling_sand = sand_start
        falling = True

        while falling:

            #try going straight down
            peek = (falling_sand[0], falling_sand[1] + 1)
            if peek not in cave and peek not in sand:
                falling_sand = peek

            #try going down and left
            elif (peek[0] - 1, peek[1]) not in cave and (peek[0] - 1, peek[1]) not in sand:
                falling_sand =  (peek[0] - 1, peek[1])

            #try going down and right
            elif (peek[0] + 1, peek[1]) not in cave and (peek[0] + 1, peek[1]) not in sand:
                falling_sand = (peek[0] + 1, peek[1])

            #can't move anymore. Sand comes to a rest
            else:
                sand.add(falling_sand)
                falling = False

            if falling_sand[1] > floor: 
                break

        #if we didn't add any sand then the simulation is complete
        if len(sand) == len_last_sand:
            break
        else:
            len_last_sand = len(sand)
            
    print(len(sand))

    return 1

def main() -> int:

    cave: Set[Rock] = set()

    sand_start = (500,0)

    for line in sys.stdin:
        r = [tuple([int(i) for i in rock.strip().split(',')]) for rock in line.strip().split('->')]
        cave = cave.union(build_cave(r))

    fill_cave(sand_start, cave)
    fill_cave2(sand_start, cave)

    return 1

if __name__ == '__main__':
    sys.exit(main())
