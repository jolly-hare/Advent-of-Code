import time


def parse(file_input):
    parsed_data = [i.rstrip("\n") for i in file_input.readlines()]
    print(f"parsing_data[:4]: {parsed_data[:4]}")
    return parsed_data


def part1(data):
    # solution for Part 1 here
    ans = 0
    for a in data:
        for b in a:
            if not b.isalpha():
                dig1 = b
                break
        for c in a[::-1]:
            if not c.isalpha():
                dig2 = c
                break
        ans += int(dig1 + dig2)
    return ans


def part2(data):
    # solution for Part 2 here
    ans = 0
    for a in data:
        dig1 = 0
        dig2 = 0
        a = a.replace("one", "o1ne")
        a = a.replace("two", "t2wo")
        a = a.replace("three", "t3hree")
        a = a.replace("four", "f4our")
        a = a.replace("five", "f5ive")
        a = a.replace("six", "s6ix")
        a = a.replace("seven", "s7even")
        a = a.replace("eight", "e8ight")
        a = a.replace("nine", "n9ine")
        for b in a:
            if not b.isalpha():
                dig1 = b
                break
        for c in a[::-1]:
            if not c.isalpha():
                dig2 = c
                break
        ans += int(dig1 + dig2)
    return ans


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Solve for example data
    ex_file = "01.example2"  # different example data for part 2; TODO: allow for diff example data
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    header = f'{"*"*5} Day 01 Examples {"*"*5}'
    print(
        f"{header}\n"
        f"  part 1: {ex_solutions[0]}\n"
        f'  part 2: {ex_solutions[1]}\n{"*"*len(header)}\n'
    )
    # assert ex_solutions == (142, 281)

    # Solve for input data
    inputfile = "01.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    header = f'{"*" * 5} Day 01 Solution {"*" * 5}'
    print(
        f"{header}\n"
        f'  part 1: {solutions[0]}\n'
        f'  part 2: {solutions[1]}\n{"*"*len(header)}\n'
        f'   submit answer here: https://adventofcode.com/$YEAR/day/$DAY'
    )
    assert solutions == (54968, 54094)
    elapsed_time = time.perf_counter() - start_time
    print(f"Run time: {elapsed_time*1000:.4f} milliseconds")
