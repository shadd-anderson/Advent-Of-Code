import fileinput

lines = list(fileinput.input('6.txt'))
data = set((int(x.split(', ')[0]), int(x.split(', ')[1])) for x in lines)
max_x = max(x[0] for x in data)
max_y = max(y[1] for y in data)


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def closest(a, dict_of_points):
    index = set()
    close_dist = 10000000
    for x, b in dict_of_points.items():
        if distance(a, b) < close_dist:
            close_dist = distance(a, b)
            index.clear()
            index.add(x)
        elif distance(a, b) == close_dist:
            index.add(x)
    return index


def part1():
    points = dict(map(lambda point, x: (point, x), range(len(data)), data))
    copy_points = dict(points)
    areas = dict()
    for x in range(max_x):
        for y in range(max_y):
            closest_point = closest((x, y), points)
            if len(closest_point) > 1:
                continue
            else:
                closest_point = closest_point.pop()

            if x == 0 or y == 0:
                    copy_points.pop(closest_point, None)
            else:
                if closest_point in copy_points:
                    areas[closest_point] = areas.setdefault(closest_point, 0) + 1
                else:
                    areas.pop(closest_point, None)
    return max(areas.values())


def part2():
    safe_zone = 0
    for x in range(max_x):
        for y in range(max_y):
            if sum(distance((x, y), point) for point in data) < 10000:
                safe_zone += 1

    return safe_zone


print(part1())
# 4589

print(part2())
# 40252
