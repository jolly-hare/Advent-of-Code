import time
from copy import deepcopy


def parse(file_input):
    commands = []
    for i in file_input:
        if i[0] != '#':
            splits = i.split(' ')
            segments = [int(x) for x in (splits[1], splits[3], splits[5])]
            commands.append(segments)
    return commands


def part1(stacks, commands):
    for i in commands:
        a = 1
        src = i[1] - 1
        dst = i[2] - 1
        while a <= i[0]:
            stacks[dst].extend(stacks[src].pop())
            a += 1
    tops = []
    for i in stacks:
        tops.append(i.pop())
    return ''.join(tops)


def part2(stacks, commands):
    for i in commands:
        num = i[0]
        src = i[1] - 1
        dst = i[2] - 1
        letters = stacks[src][-num:]
        del stacks[src][-num:]
        stacks[dst].extend(letters)
    tops = []
    for i in stacks:
        tops.append(i.pop())
    return ''.join(tops)


def solve(stacks, commands):
    solution1 = part1(deepcopy(stacks), commands)
    solution2 = part2(deepcopy(stacks), commands)
    return solution1, solution2


if __name__ == "__main__":
    start_time = time.perf_counter()
    ex_file = "05.example"
    ex_stacks = [['Z', 'N'],
                 ['M', 'C', 'D'],
                 ['P']]
    with open(ex_file, "r") as f1:
        commands = parse(f1)
    ex_solutions = solve(ex_stacks, commands)
    print(f'{"*" * 5} Examples {"*" * 5}\n'
          f'  part 1: {ex_solutions[0]}\n'
          f'  part 2: {ex_solutions[1]}\n{"*" * 20}\n')
    assert ex_solutions == ('CMZ', 'MCD')

    inputfile = "05.input"
    stacks = [['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
              ['T', 'B', 'M', 'Z', 'R'],
              ['Z', 'L', 'C', 'H', 'N', 'S'],
              ['S', 'C', 'F', 'J'],
              ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
              ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
              ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
              ['M', 'Z', 'R'],
              ['M', 'C', 'L', 'G', 'V', 'R', 'T']]
    with open(inputfile, "r") as f2:
        commands = parse(f2)
    solutions = solve(stacks, commands)
    print(f'{"*" * 5} Solution {"*" * 5}\n'
          f'  part 1: {solutions[0]}\n'
          f'  part 2: {solutions[1]}\n{"*" * 20}')
    elapsed_time = time.perf_counter() - start_time
    print(f'Run time: {elapsed_time:.4f} seconds')
