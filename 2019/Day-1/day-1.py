import fileinput
import math

lines = list(int(line) for line in fileinput.input('1.txt'))


def part1():
    return sum((math.floor(line / 3 - 2) for line in lines))


def part2():
    total = 0
    for line in lines:
        more_fuel = True
        fuel = line
        while more_fuel:
            fuel_needed = math.floor(fuel / 3) - 2
            if fuel_needed > 0:
                total += fuel_needed
                fuel = fuel_needed
            else:
                more_fuel = False
    return total


print(part1())
# 3465154

print(part2())
# 5194864
