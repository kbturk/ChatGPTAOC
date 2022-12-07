import sys, argparse
from typing import List


def main(args: List[str]):
    input_string = sys.stdin.read().replace("\n","")
    #Parse the input into a list of tuples of the form (start, end)
    pairs = [(int(pair.split('-')[0]), int(pair.split('-')[1])) for pair in input_string.split(',')]
    print(pairs)
    # Keep track of the number of overlapping pairs
    overlapping_pairs = 0

    # Iterate over all pairs of pairs
    for i in range(0, len(pairs), 2):
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
