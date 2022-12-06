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
        round_score = 0
        if choices[1] == "X":
            # If the round needs to end in a loss, choose Rock
            round_score = 1 + round_outcome("X", choices[0])
        elif choices[1] == "Y":
            # If the round needs to end in a draw, choose the same shape as the opponent
            round_score = 2 + round_outcome(choices[0], choices[0])
        elif choices[1] == "Z":
            # If the round needs to end in a win, choose the shape that defeats the opponent's shape
            if choices[0] == "A":
                round_score = 3 + round_outcome("Y", choices[0])
            elif choices[0] == "B":
                round_score = 3 + round_outcome("X", choices[0])
            elif choices[0] == "C":
                round_score = 3 + round_outcome("Z", choices[0])

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

