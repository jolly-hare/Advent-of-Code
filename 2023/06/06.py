import time


def parse(file_input):
    parsed_data = [i.rstrip("\n") for i in file_input.readlines()]
    print(f'parse check: {parsed_data[:10]}')
    return parsed_data


def part1(data):
    # solution for Part 1 here
    t1, d1 = [x.split() for x in data]
    t = [int(x) for x in t1 if ":" not in x]
    d = [int(x) for x in d1 if ":" not in x]
    for x in range(len(t)):
        print(f'race: t={t[x]}, d={d[x]}')
    # parsing works!

    return None


def part2(data):
    # solution for Part 2 here
    return None


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
    assert ex_solutions == (None, None)
    header = f'{"*"*5} Day 06 Examples {"*"*5}'
    print(f'{header}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: {ex_solutions[1]}\n{"*"*len(header)}\n')

    inputfile = "06.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    assert solutions == (None, None)
    header = f'{"*" * 5} Day 06 Solution {"*" * 5}'
    print(f'{header}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: {solutions[1]}\n{"*"*len(header)}\n'
          f'  submit answer here: https://adventofcode.com/2023/day/6')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time*1000:.4f} milliseconds')
