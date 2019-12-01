import fileinput

lines = list(fileinput.input('3.txt'))
plans = [x.split() for x in lines]
for plan in plans:
    temp_plan = plan
    temp_plan[2] = [x.replace(':', '') for x in plan[2].split(',')]
    temp_plan[3] = plan[3].split('x')
    plan = temp_plan


def part1():
    touched_fabric = set()
    overlaps = set()
    for plan in plans:
        start_x, start_y = int(plan[2][0]), int(plan[2][1])
        width, height = int(plan[3][0]), int(plan[3][1])
        for tall in range(start_y, start_y + height):
            for wide in range(start_x, start_x + width):
                inch = (tall, wide)
                if inch in touched_fabric:
                    overlaps.add(inch)
                else:
                    touched_fabric.add(inch)

    return len(overlaps)


def part2():
    coordinates = dict()
    for plan in plans:
        current_plan = plan[0]
        start_x, start_y = int(plan[2][0]), int(plan[2][1])
        width, height = int(plan[3][0]), int(plan[3][1])
        for tall in range(start_y, start_y + height):
            for wide in range(start_x, start_x + width):
                try:
                    coordinates[(tall, wide)].append(current_plan)
                except KeyError:
                    coordinates.setdefault((tall, wide), list())
                    coordinates[(tall, wide)].append(current_plan)
                except AttributeError:
                    coordinates.setdefault((tall, wide), list())
                    coordinates[(tall, wide)].append(current_plan)

    all_plans = [x[0] for x in plans]
    for coordinate in coordinates.keys():
        if len(coordinates[coordinate]) != 1:
            for a_plan in coordinates[coordinate]:
                try:
                    all_plans.remove(a_plan)
                except ValueError:
                    pass
    return all_plans[0]


print(part1())
# 111485

print(part2())
# #113
