def parse(file_input):
    input_file = [i.replace(" ", "").strip() for i in file_input.readlines()]
    return [line for line in input_file]


def part1(data):
    # Rules: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    # Play: A,X=rock; B,Y=paper; C,Z=scissor
    # My score: 1 for Rock, 2 for Paper, and 3 for Scissors
    # Outcome: 0 if lost, 3 if draw, 6 if won
    myscores = {'X': 1, 'Y': 2, 'Z': 3}
    outcomes = {'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}
    totalscore = 0
    for i in range(len(data)):
        totalscore += outcomes[data[i]] + myscores[data[i][1]]
    return totalscore


def part2(data):
    # new Play: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    myscores = {'X': 1, 'Y': 2, 'Z': 3}
    outcomes = {'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}
    choose = {'AX': 'Z', 'AY': 'X', 'AZ': 'Y', 'BX': 'X', 'BY': 'Y', 'BZ': 'Z', 'CX': 'Y', 'CY': 'Z', 'CZ': 'X'}
    totalscore = 0
    for i in range(len(data)):
        toplay = choose[data[i]]
        totalscore += myscores[toplay] + outcomes[data[i][0]+toplay]
    return totalscore


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    file = "02.input"  # input example
    with open(file, "r") as f:
        puzzle_parsed = parse(f)
    print(f'using file: {file}\nparse check: {puzzle_parsed[:10]}')
    solutions = solve(puzzle_parsed)
    print(f'\n{"*"*20}\n  part 1: {solutions[0]}\n  part 2: {solutions[1]}\n{"*"*20}')
