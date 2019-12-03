import fileinput

lines = list(fileinput.input('3.txt'))
wire1 = [x for x in lines[0].split(',')]
wire2 = [x for x in lines[1].split(',')]
crosses = set()


def part1():
    wire1_locations = set()
    wire2_locations = set()
    wire1_spot = (0, 0)
    wire2_spot = (0, 0)
    for move in wire1:
        direction = move[0]
        amount = int(move[1:])
        if direction == "R":
            for _ in range(amount):
                wire1_spot = (wire1_spot[0], wire1_spot[1] + 1)
                wire1_locations.add(wire1_spot)
        elif direction == "L":
            for _ in range(amount):
                wire1_spot = (wire1_spot[0], wire1_spot[1] - 1)
                wire1_locations.add(wire1_spot)
        elif direction == "U":
            for _ in range(amount):
                wire1_spot = (wire1_spot[0] + 1, wire1_spot[1])
                wire1_locations.add(wire1_spot)
        else:
            for _ in range(amount):
                wire1_spot = (wire1_spot[0] - 1, wire1_spot[1])
                wire1_locations.add(wire1_spot)

    for move in wire2:
        direction = move[0]
        amount = int(move[1:])
        if direction == "R":
            for _ in range(amount):
                wire2_spot = (wire2_spot[0], wire2_spot[1] + 1)
                wire2_locations.add(wire2_spot)
        elif direction == "L":
            for _ in range(amount):
                wire2_spot = (wire2_spot[0], wire2_spot[1] - 1)
                wire2_locations.add(wire2_spot)
        elif direction == "U":
            for _ in range(amount):
                wire2_spot = (wire2_spot[0] + 1, wire2_spot[1])
                wire2_locations.add(wire2_spot)
        else:
            for _ in range(amount):
                wire2_spot = (wire2_spot[0] - 1, wire2_spot[1])
                wire2_locations.add(wire2_spot)

    for location in wire1_locations:
        if location in wire2_locations:
            crosses.add(location)

    min_distance = 1000000
    for location in crosses:
        distance = abs(location[0]) + abs(location[1])
        if distance < min_distance:
            min_distance = distance

    return min_distance


def part2():
    wire1_spot = (0, 0)
    wire2_spot = (0, 0)
    shortest_distances1 = {x: 0 for x in crosses}
    shortest_distances2 = {x: 0 for x in crosses}
    wire1_travel = 0
    wire2_travel = 0
    for move in wire1:
        direction = move[0]
        amount = int(move[1:])
        if direction == "R":
            for _ in range(amount):
                wire1_spot = (wire1_spot[0], wire1_spot[1] + 1)
                wire1_travel += 1
                if wire1_spot in crosses:
                    if shortest_distances1[wire1_spot] == 0:
                        shortest_distances1[wire1_spot] = wire1_travel
        elif direction == "L":
            for _ in range(amount):
                wire1_spot = (wire1_spot[0], wire1_spot[1] - 1)
                wire1_travel += 1
                if wire1_spot in crosses:
                    if shortest_distances1[wire1_spot] == 0:
                        shortest_distances1[wire1_spot] = wire1_travel
        elif direction == "U":
            for _ in range(amount):
                wire1_spot = (wire1_spot[0] + 1, wire1_spot[1])
                wire1_travel += 1
                if wire1_spot in crosses:
                    if shortest_distances1[wire1_spot] == 0:
                        shortest_distances1[wire1_spot] = wire1_travel
        else:
            for _ in range(amount):
                wire1_spot = (wire1_spot[0] - 1, wire1_spot[1])
                wire1_travel += 1
                if wire1_spot in crosses:
                    if shortest_distances1[wire1_spot] == 0:
                        shortest_distances1[wire1_spot] = wire1_travel

    for move in wire2:
        direction = move[0]
        amount = int(move[1:])
        if direction == "R":
            for _ in range(amount):
                wire2_spot = (wire2_spot[0], wire2_spot[1] + 1)
                wire2_travel += 1
                if wire2_spot in crosses:
                    if shortest_distances2[wire2_spot] == 0:
                        shortest_distances2[wire2_spot] = wire2_travel
        elif direction == "L":
            for _ in range(amount):
                wire2_spot = (wire2_spot[0], wire2_spot[1] - 1)
                wire2_travel += 1
                if wire2_spot in crosses:
                    if shortest_distances2[wire2_spot] == 0:
                        shortest_distances2[wire2_spot] = wire2_travel
        elif direction == "U":
            for _ in range(amount):
                wire2_spot = (wire2_spot[0] + 1, wire2_spot[1])
                wire2_travel += 1
                if wire2_spot in crosses:
                    if shortest_distances2[wire2_spot] == 0:
                        shortest_distances2[wire2_spot] = wire2_travel
        else:
            for _ in range(amount):
                wire2_spot = (wire2_spot[0] - 1, wire2_spot[1])
                wire2_travel += 1
                if wire2_spot in crosses:
                    if shortest_distances2[wire2_spot] == 0:
                        shortest_distances2[wire2_spot] = wire2_travel

    distances = set()
    for location in shortest_distances1:
            distances.add(shortest_distances1[location] + shortest_distances2[location])

    return min(distances)


print(part1())
# 1983

print(part2())
# 107754
