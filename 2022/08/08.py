import time
import numpy as np


def parse(file_input):
    parsed_data = [i.rstrip("\n") for i in file_input.readlines()]
    data = np.array([[int(digit) for digit in line] for line in parsed_data])

    return data


def part1(data):
    r = len(data)
    c = len(data[0])
    p1 = 0
    for x in range(1, r - 1):
        for y in range(1, c - 1):
            up = np.amax(data[:x, y]) < data[x, y]
            down = np.amax(data[x + 1:r, y]) < data[x, y]
            left = np.amax(data[x, :y]) < data[x, y]
            right = np.amax(data[x, y + 1:c]) < data[x, y]
            if any([up, down, left, right]):
                p1 += 1
    return p1 + (r * 2) + (c * 2) - 4


def part2(data):
    r = len(data)
    c = len(data[0])
    p2 = 0
    for x in range(1, r - 1):
        for y in range(1, c - 1):
            tree = data[x, y]
            trees = [0, 0, 0, 0]
            for z1 in np.flip(data[:x, y]):  # up
                trees[0] += 1
                if z1 >= tree:
                    break
            for z2 in data[x + 1:r, y]:  # down
                trees[1] += 1
                if z2 >= tree:
                    break
            for z3 in np.flip(data[x, :y]):  # left
                trees[2] += 1
                if z3 >= tree:
                    break
            for z4 in data[x, y + 1:c]:  # right
                trees[3] += 1
                if z4 >= tree:
                    break
            p2 = max(p2, np.prod(trees))
    return p2


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = "08.example"
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    header = f'{"*" * 5} Day 08 Examples {"*" * 5}'
    print(f'{header}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: {ex_solutions[1]}\n{"*" * len(header)}\n')
    assert ex_solutions == (21, 8)

    inputfile = "08.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    header = f'{"*" * 5} Day 08 Solution {"*" * 5}'
    print(f'{header}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: {solutions[1]}\n{"*" * len(header)}')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time * 1000:.4f} milliseconds')
