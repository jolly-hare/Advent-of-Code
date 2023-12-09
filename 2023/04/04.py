import time


def parse(file_input):
    parsed_data = [i.rstrip("\n") for i in file_input.readlines()]
    #print(f'parse check: {parsed_data[:10]}')
    return parsed_data


def part1(data):
    # solution for Part 1 here
    ans = 0
    for card in data:
        winning_numbers = [x for x in card.split(': ')[1].split(' | ')[0].strip().split(' ') if x]
        my_numbers = [x for x in card.split(": ")[1].split(" | ")[1].strip().split(" ") if x]
        winner = sum(1 for x in my_numbers if x in winning_numbers)
        ans += 2**(winner-1) if winner > 0 else 0
    return ans


def part2(data):
    # solution for Part 2 here
    cards = [1] * len(data)
    for i, card in enumerate(data):
        winning_numbers = [x for x in card.split(": ")[1].split(" | ")[0].strip().split(" ") if x]
        my_numbers = [x for x in card.split(': ')[1].split(' | ')[1].strip().split(' ') if x]
        winner = sum(1 for x in my_numbers if x in winning_numbers)
        for j in range(i+1, i+1+winner):
            cards[j] += cards[i]
    return sum(cards)


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
    #assert ex_solutions == (13, 30)
    header = f'{"*"*5} Day 04 Examples {"*"*5}'
    print(f'{header}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: {ex_solutions[1]}\n{"*"*len(header)}\n')

    inputfile = "04.input"
    with open(inputfile, "r") as f2:
        input_parsed = parse(f2)
    solutions = solve(input_parsed)
    #assert solutions == (23673, 12263631)
    header = f'{"*" * 5} Day 04 Solution {"*" * 5}'
    print(f'{header}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: {solutions[1]}\n{"*"*len(header)}\n'
          f'  submit answer here: https://adventofcode.com/2023/day/8')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time*1000:.4f} milliseconds')
