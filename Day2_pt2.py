import sys

strategy_guide = [tuple(l.strip().split(' ')) for l in sys.stdin]
number_of_rounds = len(strategy_guide)
my_shape = None
score = 0
# Initialize variables
total_score = 0
opponent_shape = ''
outcome = ''

# Loop for as many rounds as there are in the game
for i in range(number_of_rounds):
    # Read the opponent's shape and the outcome of the round from the strategy guide
    opponent_shape, outcome = strategy_guide[i]

    # Choose your shape based on the opponent's shape and the outcome of the round
    if opponent_shape == 'A':
        if outcome == 'Z':
            my_shape = 'B'
        elif outcome == 'X':
            my_shape = 'C'
    elif opponent_shape == 'B':
        if outcome == 'Z':
            my_shape = 'C'
        elif outcome == 'X':
            my_shape = 'A'
    elif opponent_shape == 'C':
        if outcome == 'Z':
            my_shape = 'A'
        elif outcome == 'X':
            my_shape = 'B'

    # Calculate your score for the round
    if my_shape == 'A':
        score = 1
    elif my_shape == 'B':
        score = 2
    elif my_shape == 'C':
        score = 3

    if outcome == 'Z':
        score += 6
    elif outcome == 'Y':
        score += 3

    # Add your score for the round to your total score
    total_score += score

# Print your total score
print(total_score)

