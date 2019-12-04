import day7
import fileinput
import unittest

final_string = day7.part1()
lines = list(fileinput.input('7.txt'))
instructions = {(line.split()[1], line.split()[7]) for line in lines}


class StepOrganizerTests(unittest.TestCase):
    def test_valid_instructions(self):
        for instruction in instructions:
            self.assertLess(final_string.find(instruction[0]), final_string.find(instruction[1]),
                            "{} is not before {}!".format(instruction[0], instruction[1]))

    def test_alphabetical(self):
        for x, letter in enumerate(final_string[:-1]):
            next_letter = final_string[x+1]
            if letter > next_letter:
                self.assertIn((letter, next_letter), instructions, "{} is out of order!".format(letter))


if __name__ == "__main__":
    unittest.main()
