import time
import numpy as np


def parse(file_input):
    parsed_data = [list(i.rstrip("\n")) for i in file_input.readlines()]
    data_array = np.array(parsed_data, dtype="str")
    pad_array = np.pad(data_array, [1, 1], mode="constant", constant_values=".")
    data = pad_array.tolist()
    # print("parse check:")
    # for num in range(3):
    #     print(f"Line {num}, {type(data[num])}|{data[num]}")
    return data


def part1(data):
    # solution for Part 1 here
    # sum numbers adjacent, even diagonally, to a symbol (not .)
    neighbors = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
    ans = 0
    for y, row in enumerate(data):
        print(f'\nrow {y}: {row}')
        for x, val in enumerate(row):
            is_counted = False
            if val.isdigit():
                for dx, dy in neighbors:
                    n = data[x+dx][y+dy]
                    if not n.isdigit() and n != '.':
                        print(f'r:{row} val:{val} dx: {dx} dy:{dy} data:{data[x+dx][y+dy]}')
                        is_counted = True
                        break
            if is_counted:
                # get full number
                is_counted = True
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
    ex_file = "03.example"
    # 03.example2: part1 = 925, part2 = 6756
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    assert ex_solutions == (None, None)
    header = f'{"*"*5} Day 03 Examples {"*"*5}'
    print(
        f"{header}\n"
        f"  part 1: {ex_solutions[0]}\n"
        f'  part 2: {ex_solutions[1]}\n{"*"*len(header)}\n'
    )
    exit()
    inputfile = "03.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    assert solutions == (None, None)
    header = f'{"*" * 5} Day 03 Solution {"*" * 5}'
    print(
        f"{header}\n"
        f"  part 1: {solutions[0]}\n"
        f'  part 2: {solutions[1]}\n{"*"*len(header)}\n'
        f"  submit answer here: t33ocvs"
    )
    elapsed_time = time.perf_counter() - start_time
    print(f"Run time: {elapsed_time*1000:.4f} milliseconds")
