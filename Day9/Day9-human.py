from copy import deepcopy
import sys
from typing import List, Tuple, Set

def update_tail(H: Tuple[int,int], T: Tuple[int,int]) -> Tuple[int,int]:
    #1) H & T in the same col
    if H[0] == T[0]:
        if abs(H[1] - T[1]) > 1:
            if T[1] > H[1]: T[1] -= 1
            if T[1] < H[1]: T[1] += 1
            return T

    #2) H & T in the same row
    if H[1] == T[1]:
        if abs(H[0] - T[0]) > 1:
            if T[0] > H[0]: T[0] -= 1
            if T[0] < H[0]: T[0] += 1
            return T

    if abs(H[0] - T[0]) + abs(H[1] - T[1]) > 2:
        #adjust row:
        if T[1] > H[1]: T[1] -= 1
        if T[1] < H[1]: T[1] += 1

        #adjust col:
        if T[0] > H[0]: T[0] -= 1
        if T[0] < H[0]: T[0] += 1

    return T

def main():
    H = [0,0]
    T = [0,0]
    part_2 = list([0,0] for i in range(10))
    print(part_2)
    tail_seen = set((0,0))
    tail_seen2 = set((0,0))
    moves = [line.strip('\n').split() for line in sys.stdin]
    for move in moves:
        direction = move[0]
        spaces = int(move[1])
        for i in range(1,spaces+1):
            match direction:
                case 'R':
                    H[0] += 1
                case 'L':
                    H[0] -= 1
                case 'U':
                    H[1] -= 1
                case 'D':
                    H[1] += 1
            T = update_tail(H,T)
            part_2[0] = H
            for i in range(1,len(part_2)):
                print(i-1,i)
                update_tail(part_2[i-1],part_2[i])
            #print(f'h: {H}, t: {T}')
            tail_seen.add((T[0],T[1]))
            tail_seen2.add((part_2[-1][0],part_2[-1][1]))

    print(len(tail_seen)-1)
    print(len(tail_seen2)-1)

    return 1

if __name__ == '__main__':
    sys.exit(main())
