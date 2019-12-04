criteria = "265275-781584"
puz_range = (int(criteria.split("-")[0]), int(criteria.split("-")[1]))


def part1():
    answers = set()
    for num in range(puz_range[0], puz_range[1]):
        adjacent = False
        num_str = str(num)
        for x, digit in enumerate(num_str[:-1]):
            if digit == num_str[x+1]:
                adjacent = True
        if not adjacent:
            continue

        decreasing = True
        for x, digit in enumerate(num_str[:-1]):
            if digit > num_str[x+1]:
                decreasing = False

        if not decreasing:
            continue

        answers.add(num)

    return len(answers)


def part2():
    answers = set()
    for num in range(puz_range[0], puz_range[1]):
        adjacent = False
        num_str = str(num)
        adjacents = set()
        for x, digit in enumerate(num_str[:-1]):
            if digit == num_str[x+1]:
                adjacent = True
                adjacents.add(digit)

        if 2 not in {num_str.count(x) for x in adjacents}:
            adjacent = False
        if not adjacent:
            continue

        decreasing = True
        for x, digit in enumerate(num_str[:-1]):
            if digit > num_str[x + 1]:
                decreasing = False

        if not decreasing:
            continue

        answers.add(num)

    return len(answers)


print(part1())
# 960

print(part2())
# 626
