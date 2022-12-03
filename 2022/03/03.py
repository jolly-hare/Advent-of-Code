import time


def parse(file_input):
    parsed_data = [(x[:len(x)//2].strip(), x[len(x)//2:].strip()) for x in file_input.readlines()]
    #print(f'parse check: {parsed_data[:10]}')
    return parsed_data


def part1(data):
    total = 0
    for i in data:
        letter = ''.join(set(i[0]).intersection(set(i[1])))
        priority = ord(letter) - 96
        if priority < 0:
            priority += 58
        total += priority
    return total


def part2(data):
    n = 3
    data2 = [''.join(i) for i in data]
    groups = [data2[i:i + n] for i in range(0, len(data2), n)]
    total = 0
    for i in groups:
        letter = ''.join(set(i[0]).intersection(set(i[1]), set(i[2])))
        priority = ord(letter) - 96
        if priority < 0:
            priority += 58
        total += priority
    return total


def solve(puzzle_input):
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = "03.example"
    with open(ex_file, "r") as f1:
        ex_parsed = parse(f1)
    ex_solutions = solve(ex_parsed)
    print(f'{"*"*5} Examples {"*"*5}\n  part 1: {ex_solutions[0]}\n  part 2: {ex_solutions[1]}\n{"*"*20}\n')
    assert ex_solutions == (157, 70)

    inputfile = "03.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    print(f'{"*"*5} Solution {"*"*5}\n  part 1: {solutions[0]}\n  part 2: {solutions[1]}\n{"*"*20}')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time:.2f} seconds')
