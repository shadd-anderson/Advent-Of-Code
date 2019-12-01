import fileinput

lines = list(fileinput.input('2.txt'))


def part1():
    twos = []
    threes = []
    for line in lines:
        chars = set(line)
        for char in chars:
            if line.count(char) == 2:
                if line not in twos:
                    twos.append(line)
            if line.count(char) == 3:
                if line not in threes:
                    threes.append(line)

    return len(twos) * len(threes)


def part2():
    for x, line in enumerate(lines):
        for z, next_line in enumerate(lines[x+1:], start=x+1):
            difference = 0
            differences = []
            for y, char in enumerate(line):
                if line[y] is not next_line[y]:
                    difference += 1
                    differences.append(y)
                if difference == 2:
                    break
            if difference == 1:
                line = line[:differences[0]] + line[differences[0]+1:]
                return line + " (from lines {} and {})".format(x+1, z+1)


print(part1())
# 5368

print(part2())
# cvgywxqubnuaefmsljdrpfzyi (from lines 32 and 218)
