import fileinput

lines = list(fileinput.input('2.txt'))
data = [int(x) for x in lines[0].split(",")]
processed = list(data)


def part1():
    processed[1] = 12
    processed[2] = 2
    current_command = processed[0]
    index = 0
    while current_command != 99:
        current_command = processed[index]
        if current_command == 1:
            total = processed[processed[index + 1]] + processed[processed[index + 2]]
            processed[processed[index + 3]] = total
            index += 4
        elif current_command == 2:
            total = processed[processed[index + 1]] * processed[processed[index + 2]]
            processed[processed[index + 3]] = total
            index += 4
        else:
            break

    return processed[0]


def part2():
    result = 0
    while result != 19690720:
        for x in range(100):
            for y in range(100):
                processed_copy = list(data)
                processed_copy[1] = x
                processed_copy[2] = y
                current_command = processed_copy[0]
                index = 0
                while current_command != 99:
                    current_command = processed_copy[index]
                    if current_command == 1:
                        total = processed_copy[processed_copy[index + 1]] + processed_copy[processed_copy[index + 2]]
                        processed_copy[processed_copy[index + 3]] = total
                        index += 4
                    elif current_command == 2:
                        total = processed_copy[processed_copy[index + 1]] * processed_copy[processed_copy[index + 2]]
                        processed_copy[processed_copy[index + 3]] = total
                        index += 4
                    else:
                        result = processed_copy[0]
                        break
                if result == 19690720:
                    return 100 * x + y


print(part1())
# 5434663

print(part2())
# 4559
