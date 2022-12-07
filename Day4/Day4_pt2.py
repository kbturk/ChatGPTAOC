import sys, argparse
from typing import List


def main(args: List[str]):
    input_string = sys.stdin.read()
    print(input_string)
    

    # Parse the input into a list of tuples of the form (start, end)
    input_string = input_string.replace('\n', ',')
    input_string = input_string[:-1]
    pairs = [(int(pair.split('-')[0]), int(pair.split('-')[1])) for pair in input_string.split(',')]

    # Keep track of the number of overlapping pairs
    overlapping_pairs = 0

    # Iterate over all pairs of pairs
    for i in range(0, len(pairs), 2):
        # Check if there is another pair available
        if i + 1 >= len(pairs):
            break
            
        pair1 = pairs[i]
        pair2 = pairs[i + 1]

        # Check if the pairs overlap
        if pair1[0] <= pair2[1] and pair2[0] <= pair1[1]:
            overlapping_pairs += 1

    # Print the result
    print(overlapping_pairs)

    return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv))
