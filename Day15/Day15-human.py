import sys, queue, json
from typing import Optional, Tuple, TypeAlias, List, Set, Dict

Sensor: TypeAlias = Tuple[int, int]

def tuning_freq(x: int, y: int) -> int:
    return x*4000000 + y

def part1(cave_map: Dict[Sensor, int], tracked_row: int) -> int:
    tracked: Set[Tuple[int,int]] = set()
    for k,matt_distance in cave_map.items():
        #print(f'evaluating: {k}, {v}')
        if (k[1] <= tracked_row and tracked_row <= k[1] + matt_distance):
            for i in range(matt_distance):
                x, y = i, matt_distance - i
                if k[1] + y == tracked_row:
                    for j in range(x+1):
                        #print(f'adding: {k[0] + j, k[1] + y}')
                        #print(f'adding: {k[0] - j, k[1] + y}')
                        tracked.add((k[0] + j, k[1] + y))
                        tracked.add((k[0] - j, k[1] + y))

        elif (k[1] - matt_distance <= tracked_row and tracked_row <= k[1]):

            for i in range(matt_distance):
                x, y = i, matt_distance - i
                if k[1] - y == tracked_row:
                    for j in range(x+1):
                        #print(f'adding: {k[0] + j, k[1] - y}')
                        #print(f'adding: {k[0] - j, k[1] - y}')
                        tracked.add((k[0] + j, k[1] - y))
                        tracked.add((k[0] - j, k[1] - y))

    #answer to part 1:
    print(len(tracked) - 1)
    return 1

def part2(cave_map: Dict[Sensor, int], ubound: int) -> int:
    sensor_list = list(sorted(cave_map.keys()))
    for y in range(ubound + 1):
        x = 0
        while x < ubound:
            for k in sensor_list:
                if (abs(k[0] - x) + abs(k[1] - y)) <= cave_map[k]:
                    found = True
                    y_dist = abs(k[1] - y)
                    x = k[0] + (cave_map[k] - y_dist + 1)
                    #print(f'after: {x,y}')
            if not found:
                print(f'solution found: {x,y}')
                return tuning_freq(x,y)
            else:
                found = False
    #print(sensor_list)
    
    print(f'no solution found: ')
    return 0

def main() -> int:

    tracked_row =10
    ubound:int =4000000

    cave_map: Dict[Sensor, int] = {}

    for line in sys.stdin:
        _,_, sensorx, sensory, _, _, _, _, beaconx, beacony = line.strip().split()
        coords = [int(i.strip('xy=:,')) for i in [sensorx, sensory, beaconx, beacony]]
        cave_map[(coords[0], coords[1])] = abs(coords[0] - coords[2]) + abs(coords[1] - coords[3])
    #print(cave_map)
    #part1(cave_map, tracked_row)
    print(part2(cave_map, ubound))
    return 1

if __name__ == '__main__':
    sys.exit(main())
