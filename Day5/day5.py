def read_input(file_path):
    with open(file_path, 'r') as file:
        fresh_ranges = []
        ingredients = []
        passed = False
        for line in file.readlines():
            l = line.strip()
            if l == "":
                passed = True
                continue
            if passed:
                ingredients.append(l)
            else:
                fresh_ranges.append(l)
        return fresh_ranges, ingredients
    
fresh_ranges, ingredients = read_input('Day5/input.txt')

def part1(fresh_ranges, ingredients): 
    l = 0
    ing = ingredients.copy()
    fresh = 0
    for fr in fresh_ranges:
        parts = fr.split('-')
        lower = int(parts[0])
        upper = int(parts[1])
        t = []
        for i in ing:
            l += 1
            if lower <= int(i) <= upper:
                fresh += 1
            else:
                t.append(int(i))
        ing = t
    return fresh, l

print("Part 1:", part1(fresh_ranges, ingredients))
        
def part2(fresh_ranges):
    fresh_ranges.sort(key=lambda x: int(x.split('-')[0]))
    i = 1
    while i < len(fresh_ranges):
        prev = fresh_ranges[i - 1]
        curr = fresh_ranges[i]
        prev_lower = int(prev.split('-')[0])
        prev_upper = int(prev.split('-')[1])
        curr_lower = int(curr.split('-')[0])
        curr_upper = int(curr.split('-')[1])
        if curr_lower <= prev_upper:
            new_range = f"{prev_lower}-{max(prev_upper, curr_upper)}"
            fresh_ranges[i - 1] = new_range
            fresh_ranges.pop(i)
            continue
        i += 1
        
            
    fresh = 0
    for fr in fresh_ranges:
        fresh += int(fr.split('-')[1]) - int(fr.split('-')[0]) + 1
    return fresh
        
        


print("Part 2:", part2(fresh_ranges))