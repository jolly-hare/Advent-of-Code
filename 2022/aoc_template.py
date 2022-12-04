import time


def parse(file_input):
    parsed_data = [i.rstrip("\n") for i in file_input.readlines()]
    print(f'parse check: {parsed_data[:10]}')
    return parsed_data


def part1(data):
    return None


def part2(data):
    return None


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = "$0X.example"
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    print(f'{"*"*5} Examples {"*"*5}\n  part 1: {ex_solutions[0]}\n  part 2: {ex_solutions[1]}\n{"*"*20}\n')
    assert ex_solutions == (None, None)

    inputfile = "$0X.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    print(f'{"*"*5} Solution {"*"*5}\n  part 1: {solutions[0]}\n  part 2: {solutions[1]}\n{"*"*20}')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time:.4f} seconds')
