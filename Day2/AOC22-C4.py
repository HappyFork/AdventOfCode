# AOC22-C4.py
# Advent of code 2022, challenge 4

score = 0

with open( "inputd2" ) as f:            # Open input file

    lines = f.readlines()               # Get lines

    # Ugly nested ifs/matches below. I need to see how other people do this
    # Also I copied and pasted code. There's DEFINITELY a better way

    for l in lines:                     # For each line

        match l[0]:                     # Check opponent's move
            case 'A':                   # Rock,
                match l[2]:
                    case 'X':           # I need to lose
                        # To lose to rock, I throw scissors
                        round_score = 3 + 0     # 3 for scissors, 0 for losing
                    case 'Y':           # I need to draw
                        # To draw to rock, I throw rock
                        round_score = 1 + 3     # 1 for rock, 3 for drawing
                    case 'Z':           # I need to win
                        # To win to rock, I throw paper
                        round_score = 2 + 6     # 2 for paper, 6 for winning

            case 'B':                   # Paper,
                match l[2]:
                    case 'X':           # I need to lose
                        # To lose to paper, I throw rock
                        round_score = 1 + 0     # 1 for rock, 0 for losing
                    case 'Y':           # I need to draw
                        # To draw to paper, I throw paper
                        round_score = 2 + 3     # 2 for paper, 3 for drawing
                    case 'Z':           # I need to win
                        # To win to paper, I throw scissors
                        round_score = 3 + 6     # 3 for scissors, 6 for winning

            case 'C':                   # Scissors
                match l[2]:
                    case 'X':           # I need to lose
                        # To lose to scissors, I throw paper
                        round_score = 2 + 0     # 2 for paper, 0 for losing
                    case 'Y':           # I need to draw
                        # To draw to scissors, I throw scissors
                        round_score = 3 + 3     # 3 for scissors, 3 for drawing
                    case 'Z':           # I need to win
                        # To win to scissors, I throw rock
                        round_score = 1 + 6     # 1 for rock, 6 for winning

        score += round_score

print( score )