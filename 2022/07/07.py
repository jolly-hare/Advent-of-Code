import time
from collections import defaultdict


def parse(file_input):
    parsed_data = [i.rstrip("\n") for i in file_input.readlines()]
    # print(f'parse check: {parsed_data[:10]}')
    return parsed_data


def part1(data):
    allsizes = defaultdict(int)
    currentpath = []
    for cmd in data:
        words = cmd.split(" ")
        if words[0] == '$' and words[1] == 'cd':
            if words[2] == '..':
                currentpath.pop()
            else:
                currentpath.append(words[2])
        elif words[0].isnumeric():
            for i in range(1, len(currentpath)+1):
                allsizes['/'.join(currentpath[:i])] += int(words[0])
    p1 = (sum(size for size in allsizes.values() if size <= 100000))

    #part2
    need = 30000000 - (70000000 - allsizes['/'])
    p2 = (min(size for size in allsizes.values() if size >= need))
    return p1, p2


def part2(data):
    return None


def solve(puzzle_input):
    solution1, solution2 = part1(puzzle_input)
    # solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = "07.example"
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    header = f'{"*"*5} Day 07 Examples {"*"*5}'
    print(f'{header}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: {ex_solutions[1]}\n{"*"*len(header)}\n')
    assert ex_solutions == (95437, 24933642)

    inputfile = "07.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    header = f'{"*" * 5} Day 07 Solution {"*" * 5}'
    print(f'{header}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: {solutions[1]}\n{"*"*len(header)}')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time*1000:.4f} milliseconds')
