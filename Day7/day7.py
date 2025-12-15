def read_input(file_path):
    with open(file_path, 'r') as file:
        array = []
        for line in file.readlines():
            t = list(line)
            if t[-1] == '\n':
                t = t[:-1]
            array.append(t)
        return array
    
input = read_input("Day7/input.txt")

def part1(input):
    l = 0 # checking iterations, not terrible
    prev_beam_indices = []
    count = 0
    for i in range(len(input)):
        next_beam_indices = []
        for j in range(len(input[0])):
            l += 1
            cell = input[i][j]
            if cell == "S":
                next_beam_indices.append(j)
                break
            if prev_beam_indices.count(j) > 0:
                # this cell contains a beam above it
                if cell == "^":
                    count += 1
                    # split to cells next to it
                    if (j - 1) not in next_beam_indices:
                        next_beam_indices.append(j - 1)
                    if (j + 1) not in next_beam_indices:
                        next_beam_indices.append(j + 1)
                elif cell == ".":
                    if j not in next_beam_indices:
                        next_beam_indices.append(j)
                    
        prev_beam_indices = next_beam_indices
    return count, l

print("part 1: ", part1(input))

# might be a recursive solution here for every timeline
bTotals = {}

def process_beam(input, beampos, spliti):
    count = 1
    l = 0
    j = beampos
    for i in range(spliti + 1, len(input)):
        l += 1
        cell = input[i][j]
        if cell == "^":
            # split to cells next to it
            c2, l2 = 0, 0
            if (i,j+1) in bTotals:
                c2 = bTotals[(i,j+1)]
            else:
                c2, l2 = process_beam(input, j + 1, i)
            bTotals[(i,j+1)] = c2
            count += c2
            l += l2
            j -= 1

    return count, l

def part2(input):
    l = 0 # checking iterations
    count = 0 # timelines
    for j in range(len(input[0])):
        l += 1
        cell = input[0][j]
        if cell == "S":
            print("found S")
            c, l = process_beam(input, j, 0)
            count += c
            break
    return count, l

print("part 2: ", part2(input))
