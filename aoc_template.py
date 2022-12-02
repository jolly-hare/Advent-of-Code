def parse(file_input):
    input_file = [i.rstrip("\n") for i in file_input.readlines()]
    return [int(line) for line in input_file]


def part1(data):
    return None


def part2(data):
    return None


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    file = "01.example"  # input example
    with open(file, "r") as f:
        puzzle_parsed = parse(f)
    print(f'using file: {file}\nparse check: {puzzle_parsed[:10]}')
    solutions = solve(puzzle_parsed)
    print(f'\n{"*"*20}\n  part 1: {solutions[0]}\n  part 2: {solutions[1]}\n{"*"*20}')
