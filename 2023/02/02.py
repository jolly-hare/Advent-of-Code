import time


def parse(file_input):
    parsed_data = [i.rstrip("\n") for i in file_input.readlines()]
    #print(f'parse check: {parsed_data[:10]}\n')
    return parsed_data


def part1(data):
    # solution for Part 1 here
    max_red = 12
    max_green = 13
    max_blue = 14
    ans = 0
    for i in data:
        a = i.split(': ')
        game_num = a[0].split(' ')[1]
        cube_sets = a[1].split('; ')
        valid = True
        for cube_set in cube_sets:
            cubes = cube_set.split(', ')
            for cube in cubes:
                x = int(cube.split(' ')[0])
                color = cube.split(' ')[1]
                match color:
                    case "red":
                        if x > max_red:
                            valid = False
                    case "green":
                        if x > max_green:
                            valid = False
                    case "blue":
                        if x > max_blue:
                            valid = False
        if valid:
            ans += int(game_num)
    return ans


def part2(data):
    # solution for Part 2 here
    ans = 0
    for i in data:
        a = i.split(': ')
        cube_sets = a[1].split('; ')
        big_red = 1
        big_green = 1
        big_blue = 1
        for cube_set in cube_sets:
            cubes = cube_set.split(', ')
            for cube in cubes:
                x = int(cube.split(' ')[0])
                match cube.split(' ')[1]:
                    case "red":
                        big_red = max(big_red, x)
                    case "green":
                        big_green = max(big_green, x)
                    case "blue":
                        big_blue = max(big_blue, x)
        ans += big_red * big_green * big_blue
    return ans


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = ("02.example")
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    header = f'\n{"*"*5} Day 02 Examples {"*"*5}'
    print(f'{header}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: {ex_solutions[1]}\n{"*"*len(header)}\n')
    assert ex_solutions == (8, 2286)

    inputfile = "02.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    header = f'{"*" * 5} Day 02 Solution {"*" * 5}'
    print(f'{header}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: {solutions[1]}\n{"*"*len(header)}')
    elapsed_time = time.perf_counter() - start_time
    print(f'\nRun time: {elapsed_time*1000:.4f} milliseconds')
