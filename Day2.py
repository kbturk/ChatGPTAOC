# Create a dictionary that maps from choices to their corresponding scores
SCORES = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

# Define a function that calculates the outcome of a round
def round_outcome(p1, p2):
    # If both players choose the same shape, the round ends in a draw
    if p1 == p2:
        return 3
    # Otherwise, determine the winner
    elif (p1 == "A" and p2 == "C") or (p1 == "B" and p2 == "A") or (p1 == "C" and p2 == "B"):
        return 0
    else:
        return 6

# Define a function that calculates the total score
def total_score(strategy):
    # Split the strategy into a list of rounds
    rounds = strategy.strip().split("\n")

    # Initialize the total score to 0
    total_score = 0

    # Iterate over the rounds
    for round in rounds:
        # Split the round into a list of choices
        choices = round.strip().split()

        # Calculate the score for the round
        round_score = SCORES[choices[0]] + SCORES[choices[1]] + round_outcome(choices[0], choices[1])

        # Add the round score to the total score
        total_score += round_score

    # Return the total score
    return total_score

# Define the input strategy
strategy = """
A Y
B X
C Z
"""

# Calculate and print the total score
print(total_score(strategy))
