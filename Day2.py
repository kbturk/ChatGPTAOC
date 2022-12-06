import sys
# Create a dictionary that maps from the player's choices to their corresponding scores
SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

# Define a function that calculates the outcome of a round
def round_outcome(p1, p2):
    # If both players choose the same shape, the round ends in a draw
    if (p1 == "X" and p2 == "A") or (p1 == "Y" and p2 == "B") or (p1 == "Z" and p2 == "C"):
        return 3
    # Otherwise, determine the winner
    elif (p1 == "X" and p2 == "C") or (p1 == "Y" and p2 == "A") or (p1 == "Z" and p2 == "B"):
        return 6
    else:
        return 0

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
        round_score = SCORES[choices[1]] + round_outcome(choices[1], choices[0])

        # Add the round score to the total score
        total_score += round_score

    # Return the total score
    return total_score

# Define the input strategy
strategy = "".join([line for line in sys.stdin])

# Calculate and print the total score
print(total_score(strategy))

