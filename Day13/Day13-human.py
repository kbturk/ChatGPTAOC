import sys, queue, json
from typing import Optional, Tuple, TypeAlias, List, Set
from functools import cmp_to_key

Packet: TypeAlias = int | list['Packet']

def compare(left: Packet, right: Packet) -> bool:
    match left, right:
        case (int(m), int(n)):
            return m - n
        case (int(m), right):
            return compare([m], right)
        case (left, int(n)):
            return compare(left, [n])
        case ([],[]):
            return 0
        case ([_, *_], []):
            return 1
        case ([], [_, *_]):
            return -1
        case ([l_head, *l_tail], [r_head, *r_tail]):
            match compare(l_head, r_head):
                case 0:
                    return compare(l_tail, r_tail)
                case c:
                    return c
        case _:
            raise ValueError(f'bad input: left: {left}, right:{right}')

def main() -> int:
    tot = 0
    pairs = 0
    left, right = None, None

    instructions = [l.strip('\n') for l in sys.stdin]

    for l in instructions:
        if l == "":
            pairs += 1
            if compare(left, right) <= 0:
                print(f'compared: {left} with {right} and found True, adding {pairs}')
                tot += pairs
            else:
                print(f'left: {left}, right: {right} found False')
            left, right = None, None
            continue
        if left == None:
            left = json.loads(l)
        elif right == None:
            right = json.loads(l)
        else:
            raise ValueError("Danger Will Robinson: {l}")
    #part 2:
    instr = [json.loads(l) for l in instructions if l != ""]
    print(instr, len(instr))
    instr.append([[2]])
    instr.append([[6]])
    instr.sort(key = cmp_to_key(compare))
    print((instr.index([[2]]) + 1) * (instr.index([[6]]) + 1))

    print(tot)
    return 1

if __name__ == '__main__':
    sys.exit(main())
