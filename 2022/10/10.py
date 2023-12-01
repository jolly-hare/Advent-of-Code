import time


def parse(file_input):
    parsed_data = [i.rstrip("\n").split() for i in file_input.readlines()]
    # print(f'parse check: {parsed_data[:10]}')
    return parsed_data


def part1(data):
    register = 1
    cycle = 0
    ans = 0
    for i in data:
        if i[0] == 'addx':
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                ans += register * cycle
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                ans += register * cycle
            register += int(i[1])
        else:  # noop
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                ans += register * cycle
    return ans


def part2(data):
    sprite_center = 2
    cycle = 1
    ans = " "
    for i in data:
        if i[0] == "addx":
            if cycle % 40 in [sprite_center - 1, sprite_center, sprite_center + 1]:
                ans += "█"
            else:
                ans += " "
            cycle += 1
            if cycle % 40 == 0:
                ans += "\n"
            if cycle % 40 in [sprite_center - 1, sprite_center, sprite_center + 1]:
                ans += "█"
            else:
                ans += " "
            cycle += 1
            sprite_center += int(i[1])
            if cycle % 40 == 0:
                ans += "\n"
        else:
            if cycle % 40 in [sprite_center - 1, sprite_center, sprite_center + 1]:
                ans += "█"
            else:
                ans += " "
            cycle += 1
            if cycle % 40 == 0:
                ans += "\n"
    return ans


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = "10.example"
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    header = f'{"*" * 5} Day 10 Examples {"*" * 5}'
    print(f'{header}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: \n{ex_solutions[1]}\n{"*" * len(header)}\n')
    # assert ex_solutions == (13140, None)

    inputfile = "10.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    header = f'{"*" * 5} Day 10 Solution {"*" * 5}'
    print(f'{header}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: \n{solutions[1]}\n{"*" * len(header)}')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time * 1000:.4f} milliseconds')
