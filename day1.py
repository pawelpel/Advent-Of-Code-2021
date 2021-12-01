# https://adventofcode.com/2021/day/1
with open('inputs/day1.txt', 'r') as f:
    given_measurements = list(map(int, f.readlines()))


def puzzle_1(measurements):
    last = measurements[0]
    count = 0

    for m in measurements[1:]:
        if m > last:
            count += 1
        last = m
    return count


print(puzzle_1(given_measurements))


def puzzle_2(measurements):
    last = sum(measurements[:3])
    count = 0
    for i in range(1, len(measurements)-2):
        tmp = sum(measurements[i:i+3])
        if tmp > last:
            count += 1
        last = tmp
    return count


print(puzzle_2(given_measurements))
