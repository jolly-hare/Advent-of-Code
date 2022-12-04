import time


def parse(file_input):
    parsed_data = [i.rstrip("\n") for i in file_input.readlines()]
    # print(f'parse check: {parsed_data[:10]}')
    return parsed_data


def part1(data):
    count = 0
    for i in data:
        elf1, elf2 = i.split(',')
        elf1a, elf1b = elf1.split('-')
        elf2a, elf2b = elf2.split('-')
        # print(elf1a, elf1b, elf2a, elf2b)
        elf1a, elf1b, elf2a, elf2b = [int(x) for x in [elf1a, elf1b, elf2a, elf2b]]
        if (elf1a >= elf2a and elf1b <= elf2b) or (elf1a <= elf2a and elf1b >= elf2b):
            count += 1
    return count


def part2(data):
    count = 0
    for i in data:
        elf1, elf2 = i.split(',')
        elf1a, elf1b = elf1.split('-')
        elf2a, elf2b = elf2.split('-')
        # print(elf1a, elf1b, elf2a, elf2b)
        elf1a, elf1b, elf2a, elf2b = [int(x) for x in [elf1a, elf1b, elf2a, elf2b]]
        if not ((elf1b < elf2a) or (elf1a > elf2b)):
            count += 1
    return count


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = "04.example"
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    print(f'{"*"*5} Examples {"*"*5}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: {ex_solutions[1]}\n{"*"*20}\n')
    assert ex_solutions == (2, 4)

    inputfile = "04.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    print(f'{"*"*5} Solution {"*"*5}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: {solutions[1]}\n{"*"*20}')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time:.4f} seconds')
