import fileinput

lines = list(fileinput.input('1.txt'))


def part1():
    frequency = 0
    for line in lines:
        frequency += int(line)
    return frequency


def part2():
    frequency = 0
    frequencies = set()
    frequencies.add(0)
    while True:
        for line in lines:
            frequency += int(line)
            if frequency in frequencies:
                return frequency
            frequencies.add(frequency)


print(part1())
# 536

print(part2())
# 75108
