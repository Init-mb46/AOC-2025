import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = []
        for line in file.readlines():
            lines.append(line)
        return lines
    
def parse_input1(input):
    lines = []
    for line in input:
        lines.append(re.sub(r"\s+", ' ', line.strip()).split(" "))
    return lines
    
def parse_input2(input):
    lines = []
    for line in input:
        lines.append(list(line))
    return lines

def compute_operation(numbers, addition):  
    t = 0
    if not addition:
        t = 1
    for n in numbers: 
        if addition:
            t += int(n)
        else:
            t *= int(n)
    return t

raw_input = read_input('Day6/input.txt')
input = parse_input1(raw_input)

def part1(input):
    tot = 0
    problems = len(input[0])
    for i in range(problems):
        problem_tot = 0
        addition = False
        if input[len(input) - 1][i] == "*":
            addition = False
            problem_tot = 1
        else:
            addition = True
        for l in range(len(input) - 1):
            line = input[l]
            if addition:
                problem_tot += int(line[i])
            else: 
                problem_tot *= int(line[i])
        tot += problem_tot
    return tot

print("Part 1:", part1(input))

# need to change the parsing, numbers need to be alighned as shown in input.

def part2(input):
    tot = 0
    charlength = len(input[0]) - 1
    numbers = []
    addition = True
    pos = 1
    for i in range(charlength):
        all_blank = True
        for x in range(len(input)):
            if input[x][i] != " ":
                all_blank = False
                
        if all_blank: 
            # one computation finished
            x = compute_operation(numbers, addition)
            tot += x
            numbers = []
            pos = 1
            continue
            
        if input[len(input) - 1][i] == "*":
            addition = False
        elif input[len(input) - 1][i] == "+":
            addition = True
            
        # parse the actual problem numbers into the numbers array
        for l in range(len(input) - 1):
            line = input[l]
            n = line[i]
            if n == " ":
                continue
            if len(numbers) < pos:
                numbers.append(n)
            else:
                numbers[pos - 1] += n    
        pos += 1 
    x = compute_operation(numbers, addition)
    tot += x
    return tot

input2 = parse_input2(raw_input)

print("Part 2: ", part2(input2))