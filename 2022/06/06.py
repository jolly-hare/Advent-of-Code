import time


def parse(file_input):
    parsed_data = file_input.readline()
    return parsed_data


def part1(data):
    buffer = [x for x in data[:4]]
    for i in range(4, len(data)):
        buffer = [x for x in data[i-4:i]]
        if len(set(buffer)) == 4:
            return i


def part2(data):
    buffer = [x for x in data[:14]]
    for i in range(14, len(data)):
        buffer = [x for x in data[i-14:i]]
        if len(set(buffer)) == 14:
            return i


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = "06.example"
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    print(f'{"*"*5} Examples {"*"*5}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: {ex_solutions[1]}\n{"*"*20}\n')
    assert ex_solutions == (7, 19)

    inputfile = "06.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    print(f'{"*"*5} Solution {"*"*5}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: {solutions[1]}\n{"*"*20}')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time:.4f} seconds')
