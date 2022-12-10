import time
import numpy as np


def parse(file_input):
    parsed_data = [i.rstrip("\n").split() for i in file_input.readlines()]
    return parsed_data


def part1(data, num):
    knots = [np.array([0, 0]) for _ in range(num)]
    move = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    visited = set()
    for direction, moves in data:
        for _ in range(int(moves)):
            knots[0] += move[direction]
            for old_knot, current_knot in zip(knots, knots[1:]):
                if max(abs(current_knot - old_knot)) > 1:
                    current_knot += np.clip((old_knot-current_knot), -1, 1)
            visited.add(tuple(knots[-1]))
    return len(visited)


def solve(puzzle_input):
    solution1 = part1(puzzle_input, 2)
    solution2 = part1(puzzle_input, 10)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = "09_2.example"  # gotta switch between part1 and part2
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    header = f'{"*"*5} Day 09 Examples {"*"*5}'
    print(f'{header}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: {ex_solutions[1]}\n{"*"*len(header)}\n')
    assert ex_solutions == (13, 36)  # p2 w p2 example data results in 36; p2 w p1 example results in 1

    inputfile = "09.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    header = f'{"*" * 5} Day 09 Solution {"*" * 5}'
    print(f'{header}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: {solutions[1]}\n{"*"*len(header)}')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time*1000:.4f} milliseconds')
