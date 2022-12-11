from copy import deepcopy
import sys
from typing import List, Tuple, Set

def cycle_signal_strength(cycle, X, sig_strength):
    if cycle == 20 or (cycle-20)%40 == 0:
        sig_strength += (cycle)*X
        print(cycle, X, sig_strength)
    return sig_strength

def pixel(X,cycle):
    if cycle%40 in [X-1, X, X+1]:
        return '#'
    return '.'

def append_pixel(X, cycle, image):
    #beginning
    char = pixel(X, cycle)
    if len(image[-1])%40 == 0:
        image.append([char])
    else:
        image[-1].append(char)
    return image

def main():
    instructions = [line.strip('\n').split() for line in sys.stdin]
    X = 1
    cycle = 0
    sig_strength = 0

    #"image" is made up of 40 character rows of '#' and '.' Characters
    image = [[]]
    char = '.'

    for item in instructions:

        if item[0] == 'noop':
            image =  append_pixel(X, cycle, image)
            cycle += 1
            sig_strength = cycle_signal_strength(cycle, X, sig_strength)

        if item[0] == 'addx':
            image =  append_pixel(X, cycle, image) #0
            cycle += 1 #1
            sig_strength = cycle_signal_strength(cycle, X, sig_strength)

            image =  append_pixel(X, cycle, image)
            cycle += 1 #2
            sig_strength = cycle_signal_strength(cycle, X, sig_strength)
            X += int(item[1])

    print(X, sig_strength)
    for line in image:
        print("".join(line))
    return 1

if __name__ == '__main__':
    sys.exit(main())
