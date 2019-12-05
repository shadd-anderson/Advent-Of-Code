import fileinput

numbers = [int(x) for x in list(fileinput.input("5.txt"))[0].split(",")]


def process_intcode(intcode, inp):
    x = 0
    while True:
        instruction = str(intcode[x])
        if len(instruction) < 5:
            instruction = ("0" * (5 - len(instruction))) + instruction
        opcode = int(instruction[-2:])
        param_1_mode = int(instruction[-3])
        param_2_mode = int(instruction[-4])

        if opcode == 1:
            first_digit = intcode[intcode[x+1]] if param_1_mode == 0 else intcode[x+1]
            second_digit = intcode[intcode[x+2]] if param_2_mode == 0 else intcode[x+2]
            intcode[intcode[x+3]] = first_digit + second_digit
            x += 4

        elif opcode == 2:
            first_digit = intcode[intcode[x + 1]] if param_1_mode == 0 else intcode[x + 1]
            second_digit = intcode[intcode[x + 2]] if param_2_mode == 0 else intcode[x + 2]
            intcode[intcode[x + 3]] = first_digit * second_digit
            x += 4

        elif opcode == 3:
            if param_1_mode == 0:
                intcode[intcode[x+1]] = inp
            else:
                intcode[x+1] = inp
            x += 2

        elif opcode == 4:
            print(intcode[intcode[x+1]] if param_1_mode == 0 else intcode[x+1])
            x += 2

        elif opcode == 5:
            test = intcode[intcode[x + 1]] if param_1_mode == 0 else intcode[x + 1]
            if test:
                x = intcode[intcode[x+2]] if param_2_mode == 0 else intcode[x+2]
            else:
                x += 3

        elif opcode == 6:
            test = intcode[intcode[x+1]] if param_1_mode == 0 else intcode[x+1]
            if not test:
                x = intcode[intcode[x+2]] if param_2_mode == 0 else intcode[x+2]
            else:
                x += 3

        elif opcode == 7:
            first_digit = intcode[intcode[x+1]] if param_1_mode == 0 else intcode[x+1]
            second_digit = intcode[intcode[x+2]] if param_2_mode == 0 else intcode[x+2]
            intcode[intcode[x+3]] = 1 if first_digit < second_digit else 0
            x += 4

        elif opcode == 8:
            first_digit = intcode[intcode[x + 1]] if param_1_mode == 0 else intcode[x + 1]
            second_digit = intcode[intcode[x + 2]] if param_2_mode == 0 else intcode[x + 2]
            intcode[intcode[x+3]] = 1 if first_digit == second_digit else 0
            x += 4

        elif opcode == 99:
            break


def part1():
    process_intcode(list(numbers), 1)


def part2():
    process_intcode(list(numbers), 5)


part1()
# 15508323

part2()
# 9006327
