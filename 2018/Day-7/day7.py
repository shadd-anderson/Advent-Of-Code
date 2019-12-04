import fileinput
import string

lines = list(fileinput.input('7.txt'))
processed = set((line.split()[1], line.split()[7]) for line in lines)
numbered_alphabet = {letter: number for number, letter in enumerate(string.ascii_uppercase)}


def part1():
    hints = {letter: set() for letter in string.ascii_uppercase}
    for line in processed:
        hints[line[0]].add(line[1])

    hints_copy = dict(hints)
    final = " "
    while len(final) < 27:
        available = set()
        for letter in hints:
            if len(hints[letter]) == len(hints[letter] & set(final.strip())):
                available.add(letter)
        final = sorted(list(available))[-1] + final
        hints_copy.pop(sorted(list(available))[-1])
        hints = dict(hints_copy)

    return final.strip()


print(part1())
