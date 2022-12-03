def parse(file_input):
    input_lines = [i.strip() for i in file_input.readlines()]
    return input_lines


def solve(puzzle_input):
    elves = list()
    cumulativesum = 0
    for i in range(0, len(puzzle_input)):
        if puzzle_input[i] == '':
            elves.append(cumulativesum)
            cumulativesum = 0
        else:
            cumulativesum += int(puzzle_input[i])
    elves_sorted = sorted(elves, reverse=True)
    return max(elves), sum(elves_sorted[:3])


if __name__ == "__main__":
    file = "01.input"
    with open(file, "r") as f:
        puzzle_parsed = parse(f)
    print(f'using file: {file}\nparse check: {puzzle_parsed[:10]}')
    solutions = solve(puzzle_parsed)
    print(f'\n{"*"*20}\n  part 1: {solutions[0]}\n  part 2: {solutions[1]}\n{"*"*20}')
