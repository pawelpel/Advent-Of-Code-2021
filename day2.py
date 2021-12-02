# https://adventofcode.com/2021/day2
with open('inputs/day2.txt', 'r') as f:
    global_commands = []
    for line in f.readlines():
        _command, _value = line.split(' ')
        global_commands.append((_command, int(_value)))


def puzzle_1(commands):
    horizontal_pos = 0
    depth = 0

    for command, value in commands:
        if command == 'forward':
            horizontal_pos += value
        elif command == 'up':
            depth -= value
        elif command == 'down':
            depth += value

    return horizontal_pos * depth


print(puzzle_1(global_commands))


def puzzle_2(commands):
    horizontal_pos = 0
    depth = 0
    aim = 0

    for command, value in commands:
        if command == 'forward':
            horizontal_pos += value
            depth += aim * value
        elif command == 'up':
            aim -= value
        elif command == 'down':
            aim += value

    return horizontal_pos * depth


print(puzzle_2(global_commands))
