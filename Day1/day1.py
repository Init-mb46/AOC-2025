import math
import itertools
import os
import collections
import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

input = read_input(os.path.join("Day1", "input.txt"))
print("Input read. Number of lines:", len(input))

start_value = 50

# any time lock lands on zero, it counts
def part1(input):
    value = start_value
    total = 0
    for line in input:
        if line.startswith('L'):
            value -= int(line[1:])
        elif line.startswith('R'):
            value += int(line[1:])
        value = value % 100
        if value == 0:
            total += 1
    return total

print("Part 1:", part1(input))

# any time lock passes or lands on zero, it counts
def part2(input):
    value = start_value
    total = 0
    for line in input:
        change = int(line[1:])
        if line.startswith('L'):
            if value - change <= 0:
                total += 1 + ((change - value) // 100)
                if value == 0 & ((value - change % 100) != 0):
                    total -= 1
            value -= change
        elif line.startswith('R'):
            if value + change >= 100:
                total += 1 + ((value + change -100) // 100)
            value += change
        value = value % 100
        # print("Current value:", value, "Total count:", total)
    return total

print ("Part 2:", part2(input))