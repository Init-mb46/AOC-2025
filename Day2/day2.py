def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.split(",") for line in file.readlines()]

productIDs = read_input("Day2/input.txt")[0]
print("Input read. Number of lines:", len(productIDs))

def parse_range(productIDs):
    ranges = []
    for (input) in productIDs:
        lower,upper = input.split("-")
        ranges.append( (int(lower), int(upper)) )
    return ranges

# part 1 is a pretty fast solution
def part1(productIDs):
    total = 0
    splits = parse_range(productIDs)
    for lower, upper in splits:
        for i in range(lower, upper+1):
            num = str(i) # string form
            if num[:len(num)//2] == num[(len(num)//2):]:
                total += i
    return total
        
print("Part 1:", part1(productIDs))

# this is actually so cursed, but it works
def part2(productIDs):
    total = 0
    splits = parse_range(productIDs)
    for lower, upper in splits:
        for i in range(lower, upper+1):
            num = str(i) # string form
            found = False
            for replength in range(1, len(num)//2 + 1):
                if found:
                    break
                if len(num) % replength != 0:
                    continue
                parts = []
                for j in range(0, len(num), replength):
                    parts.append(num[j:j+replength])
                if all(part == parts[0] for part in parts):
                    total += i
                    found = True
                    break
    return total

print ("Part 2:", part2(productIDs))