# https://adventofcode.com/2021/day3
with open('inputs/day3.txt', 'r') as f:
    diagnostic_report = f.readlines()

diagnostic_report = [list(map(int, *line.split())) for line in diagnostic_report]


def puzzle_1(report):
    row_len = len(report[0])
    counter = {k: 0 for k in range(row_len)}
    for row in report:
        for i, r in enumerate(row):
            counter[i] += r
    half = len(report) // 2
    gama_rate = ''.join(
        str(int(counter[v] > half))
        for v in range(row_len)
    )
    d = {'1': '0', '0': '1'}
    epsilon_rate = ''.join(d[v] for v in gama_rate)  # negative
    return int(gama_rate, 2) * int(epsilon_rate, 2)


print(puzzle_1(diagnostic_report))


def puzzle_2(report):
    return


print(puzzle_2(diagnostic_report))
