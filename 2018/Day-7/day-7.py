import fileinput
import string
import bisect

lines = list(fileinput.input('7.txt'))
processed = set((line.split()[1], line.split()[7]) for line in lines)
numbered_alphabet = {letter: number for number, letter in enumerate(string.ascii_uppercase)}


class Step:
    later_steps = None
    letter = None

    def __init__(self, letter):
        self.letter = letter.upper()
        self.later_steps = set()

    def __gt__(self, other):
        if self.letter in other.later_steps:
            return True
        else:
            return self.letter > other.letter

    def __lt__(self, other):
        if other.letter in self.later_steps:
            return True
        else:
            return other > self

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return other.letter == self.letter

    def __ne__(self, other):
        return self.letter != other.letter

    def __hash__(self):
        return self.letter.__hash__()

    def add_later_step(self, later_step):
        self.later_steps.add(later_step)


def part1():
    steps = list(Step(letter) for letter in string.ascii_uppercase)
    for line in processed:
        step = steps[numbered_alphabet.get(line[0])]
        step.add_later_step(line[1])
    steps.sort(key=lambda x: len(x.later_steps))
    sorted_steps = []
    for step in steps:
        bisect.bisect(sorted_steps, step)
    return "".join(step.letter for step in sorted_steps)


print(part1())
