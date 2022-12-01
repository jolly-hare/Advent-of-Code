
def parse(file_input):
    input_file = [i.strip() for i in file_input.readlines()]
    return [line for line in input_file]


def part1(data):
    elves = list()
    cumulativesum = 0
    for i in range(0, len(data)):
        if data[i] == '':
            elves.append(cumulativesum)
            cumulativesum = 0
        else:
            cumulativesum += int(data[i])
    return max(elves)


def part2(data):
    elves = list()
    cumulativesum = 0
    for i in range(0, len(data)):
        if data[i] == '':
            elves.append(cumulativesum)
            cumulativesum = 0
        else:
            cumulativesum += int(data[i])
    elves_sorted = sorted(elves, reverse=True)
    return sum(elves_sorted[:3])


def solve(puzzle_input):
    # data = parse(puzzle_input)
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    with open("01.input", "r") as f:
        puzzle_parsed = parse(f)
    print(f'parse check: {puzzle_parsed[:10]}')
    solutions = solve(puzzle_parsed)
    print(f'\npart 1: {solutions[0]}\npart 2: {solutions[1]}')
