def read_input(file_path):
    with open(file_path, 'r') as file:
        boxes = []
        lines = file.readlines()
        for line in lines:
            boxes.append(list(int(x) for x in line.strip().split(",")))
    return boxes

boxes = read_input("Day8/input.txt")

def squared_dist(box1, box2):
    s = (box1[0] - box2[0]) ** 2
    s += (box1[1] - box2[1]) ** 2
    s += (box1[2] - box2[2]) ** 2
    return s

def part1(boxes):
    t = 0
    count = 1
    pairs = []
    circuits = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            t += 1
            pairs.append((tuple(boxes[i]), tuple(boxes[j]), squared_dist(boxes[i], boxes[j])))
    pairs = sorted(pairs, key=lambda x: x[2])
    connections_left = 1000
    i = 0
    while connections_left > 0 and i < len(pairs):
        t += 1
        box1, box2, dist = pairs[i]
        circuit = False
        c_initial = 0
        for c in range(len(circuits)):
            t += 1
            if box1 in circuits[c] and box2 in circuits[c]:
                circuit = True
                connections_left -= 1
                break
            if (box1) in circuits[c] or (box2) in circuits[c]:
                if circuit:
                    circuits[c_initial] = circuits[c_initial].union(circuits[c])
                    circuits.pop(c)
                    break
                connections_left -= 1
                circuit = True
                c_initial = c
                circuits[c].add(tuple(box1))
                circuits[c].add(tuple(box2))
        if not circuit:
            connections_left -= 1
            circuits.append(set([tuple(box1), tuple(box2)]))
            
        i += 1
        
    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    for c in circuits[:3]:
        t += 1
        count *= len(c)
    return count, t

print("Part 1:", part1(boxes))

def part2(boxes):
    t = 0
    count = 0
    pairs = []
    circuits = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            t += 1
            pairs.append((tuple(boxes[i]), tuple(boxes[j]), squared_dist(boxes[i], boxes[j])))
    pairs = sorted(pairs, key=lambda x: x[2])
    i = 0
    last_two_pairs = pairs[-2:]
    while i < len(pairs):
        t += 1
        box1, box2, dist = pairs[i]
        circuit = False
        c_initial = 0
        for c in range(len(circuits)):
            t += 1
            if box1 in circuits[c] and box2 in circuits[c]:
                circuit = True
                break
            if (box1) in circuits[c] or (box2) in circuits[c]:
                if circuit:
                    circuits[c_initial] = circuits[c_initial].union(circuits[c])
                    circuits.pop(c)
                    break
                circuit = True
                c_initial = c
                circuits[c].add(tuple(box1))
                circuits[c].add(tuple(box2))
                last_two_pairs = [box1, box2]
        if not circuit:
            circuits.append(set([tuple(box1), tuple(box2)]))
            
        i += 1
    print(last_two_pairs)
    count = last_two_pairs[0][0] * last_two_pairs[1][0] 
    return count, t

print("Part 2:", part2(boxes))