import copy

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
def format_input(input):
    formatted = []
    for line in input:
        rolls = list(line)
        formatted.append(rolls)
    return formatted, len(formatted), len(formatted[0])

input = read_input('Day4/input.txt')

finput, rows, col = format_input(input)

def part1(finput, rows, col):
    valid = 0
    input_copy = copy.deepcopy(finput)  # Create a copy to avoid modifying the original during iteration
    for i in range(rows):
        for j in range(col):
            if finput[i][j] != '@':
                continue
            surrounding = 0
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if (0 <= k < rows and 0 <= l < col and not (k == i and l == j)):
                        if finput[k][l] == '@':
                            surrounding += 1
            if surrounding <= 3:
                valid += 1
                input_copy[i][j] = "#"
    return valid, input_copy

valid, edited = part1(finput, rows, col)
print("Part 1:", valid)

def part2(finput, rows, col):
    # recursively loop part1 until no more valid '@' can be found
    cinput = copy.deepcopy(finput)
    total = 0
    c, cinput = part1(cinput, rows, col)
    total += c
    while c > 0:
        c, cinput = part1(cinput, rows, col)
        total += c
    return total

print("Part 2:", part2(finput, rows, col))
            