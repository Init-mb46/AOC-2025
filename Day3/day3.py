def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
input = read_input('Day3/input.txt')

# I think this is a pretty good solution
def part1(input):
    total_voltage = 0
    for bank in input:
        batteries = [int(char) for char in bank]
        tens = batteries[0]
        ones = batteries[1]

        found_tens = False
        tens_index = 0
        for i in range(9, 0, -1):
            if found_tens:
                break
            for bindex in range(0, len(batteries)-1):
                b = batteries[bindex]
                if b == i:
                    found_tens = True
                    tens_index = bindex
                    tens = b
                    break
        
        found_ones = False
        for i in range(9, 0, -1):
            if found_ones:
                break
            for bindex in range(tens_index+1, len(batteries)):
                b = batteries[bindex]
                if b == i:
                    found_ones = True
                    ones = b
                    break
                
        total_voltage += int(str(tens) + str(ones))
        
    return total_voltage

print("Part 1:", part1(input))
        
# this solution is actually so much better than part 1 i think
def part2(input):
    total_voltage = 0
    for bank in input:
        batteries = [int(char) for char in bank]
        digits = batteries[0:12] # should have 12 at the end 
        digits_indices = [i for i in range(12)] # i found changing this (and the line above) between 2 and 12 solves part 1 and part 2
        
        # maybe try a big ahh moving window
        
        positions_left_to_search = len(batteries) - 1
        
        for i in range(1, len(batteries)):
            digit = batteries[i]
            start = len(digits) - positions_left_to_search > 0 and len(digits) - positions_left_to_search or 0
            for j in range(start, len(digits)):
                if digits_indices[j] == i:
                    # break if the battery index in the bank is the exact same one as the current window index 
                    break
                if digit > digits[j]:
                    digits[j] = digit
                    digits_indices[j] = i
                    for k in range(j+1, len(digits)):
                        digits[k] = batteries[i+(k - j)]
                        digits_indices[k] = i + (k - j)
                    break
            positions_left_to_search -= 1
            
        total_voltage += int("".join([str(d) for d in digits]))        
        
    return total_voltage

print("Part 2:", part2(input))  