import fileinput
from string import ascii_lowercase

polymer = list(fileinput.input('5.txt'))[0].strip()


def react(string):
    unreacted = ['.']
    for char in string:
        if char == unreacted[-1].swapcase():
            unreacted.pop()
        else:
            unreacted.append(char)
    return len(unreacted) - 1


def part1():
    return react(polymer)


def part2():
    return min(react(x for x in polymer if x.lower() != letter) for letter in ascii_lowercase)


print(part1())
# 11540

print(part2())
# 6918

