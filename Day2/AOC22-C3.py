# AOC22-C3.py
# Advent of code 2022, challenge 3

score = 0

with open( "inputd2" ) as f:            # Open input file

    lines = f.readlines()               # Get lines

    # Ugly nested ifs/matches below. I need to see how other people do this
    # Also I copied and pasted code. There's DEFINITELY a better way

    for l in lines:                     # For each line

        match l[2]:                     # Check my move
            case 'X':                   # Rock,
                round_score = 1         # I get 1 point for choosing Rock
                if l[0] == 'A':         # Opponent rock
                    round_score += 3    # Draw
                elif l[0] == 'C':       # Opponent scissors
                    round_score += 6    # Win
                # Else, I lose and get no additional points

            case 'Y':                   # Paper,
                round_score = 2         # I get 2 points for choosing Paper
                if l[0] == 'A':         # Opponent rock
                    round_score += 6    # Win
                elif l[0] == 'B':       # Opponent paper
                    round_score += 3    # Draw
                # Else, I lose and get no additional points

            case 'Z':                   # Scissors
                round_score = 3         # I get 3 points for choosing Scissors
                if l[0] == 'B':         # Opponent paper
                    round_score += 6    # Win
                elif l[0] == 'C':       # Opponent scissors
                    round_score += 3    # Draw
                # Else, I lose and get no additional points

        score += round_score

print( score )