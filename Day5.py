import sys, argparse
from typing import Dict, List, Set, Tuple
from enum import Enum, auto
from copy import deepcopy

class Parse_state:
    Initial = auto()
    ReadStacks = auto()
    Skip = auto()
    ReadMoves = auto()

def arg_parser():
    parser = argparse.ArgumentParser(description = 'provide input file')
    parser.add_argument('replacement_file', help = 'please provide text input file', type = argparse.FileType('r'))
    return parser

def box_parse(build_box: str, stacks: list[list[str]]) -> list[list[str]]:
    for s in stacks:
        if build_box[1].isalpha():
            s.insert(0,build_box[1])
        build_box = build_box[4:]
    return stacks

def main(args: List[str]):
    # Initialize the stacks of characters
    #stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

    # Parse the moves
    #moves = ['move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2']

    # Parse the input file
    inputs = arg_parser().parse_args(args[1:])
    instructions = [line.rstrip('\r\n') for line in inputs.replacement_file]
    state = Parse_state.Initial

    n_box_stacks = max([line.count('[') for line in instructions])
    stacks = [[] for _ in range(n_box_stacks)]

    for line in instructions:
        match state:
            case Parse_state.Initial:
                state = Parse_state.ReadStacks
                stacks = box_parse(line, stacks)
            case Parse_state.ReadStacks:
                if '[' not in line:
                    moves = instructions[instructions.index(line)+2:]
                    print(f'moves: {moves}')
                    break
                else:
                    box_parse(line, stacks)

    stacks2 = deepcopy(stacks)
    for move in moves:
        # Split the move string into its component parts
        move_parts = move.split()

        # Parse the move quantity and the source and destination stacks
        move_qty = int(move_parts[1])
        src_stack = int(move_parts[3]) - 1
        dest_stack = int(move_parts[5]) - 1

        # Move the specified number of characters from the source stack to the destination stack
        for i in range(move_qty):
            character = stacks[src_stack].pop()
            stacks[dest_stack].append(character)

        #part2:
        for i in range(move_qty):
            character = stacks2[src_stack].pop(-move_qty + i)
            stacks2[dest_stack].append(character)
    # Print the top characters of each stack
    pt1 = [stack[-1] for stack in stacks]
    pt2 = [stack[-1] for stack in stacks2]
    print("".join(pt1))
    print("".join(pt2))
    return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv))
