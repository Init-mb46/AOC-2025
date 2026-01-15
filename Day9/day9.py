def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        tiles = {}
        for line in lines:
            x, y = line.strip().split(',')
            if int(x) not in tiles:
                tiles[int(x)] = []
            tiles[int(x)].append(int(y))
        tiles = dict(sorted(tiles.items()))
        return tiles

tiles = read_input('Day9/sampleinput.txt')
            
def part1(tiles):
    i = 0
    largest_square = 0
    first_corners = []
    # first check first row
    keys = list(tiles.keys())
    for k in keys[:len(keys)//2]:
        for c in range(len(tiles[k])):
            i += 1
            first_corner = (k, tiles[k][c])
            first_corners.append(first_corner)
    
    second_corners = []
    # now check last row
    for k in keys[len(keys)//2:]:
        for c in range(len(tiles[k])):
            i += 1
            second_corner = (k, tiles[k][c])
            second_corners.append(second_corner)
        
    for fc in first_corners:
        for sc in second_corners:
            i += 1
            area = abs(sc[0] - fc[0] + 1) * abs(sc[1] - fc[1] + 1)
            if area > largest_square:
                # check if all four corners exist
                largest_square = area
    return largest_square, i

print("part 1:", part1(tiles))

def part2(tiles):
    i = 0
    largest_square = 0
    first_corners = []
    # first check first row
    keys = list(tiles.keys())
    for k in keys[:len(keys)//2]:
        for c in range(len(tiles[k])):
            i += 1
            first_corner = (k, tiles[k][c])
            first_corners.append(first_corner)
    
    second_corners = []
    # now check last row
    for k in keys[len(keys)//2:]:
        for c in range(len(tiles[k])):
            i += 1
            second_corner = (k, tiles[k][c])
            second_corners.append(second_corner)
        
    for fc in first_corners:
        for sc in second_corners:
            i += 1
            area = abs(sc[0] - fc[0] + 1) * abs(sc[1] - fc[1] + 1)
            # check opposite corners to see if the whole shape is contained within the tiles
            pass1 = False
            
            if not pass1:
                continue
            if area > largest_square:
                largest_square = area
    return largest_square, i

# print("part 2:", part2(tiles))


#https://stackoverflow.com/questions/10846431/ordering-shuffled-points-that-can-be-joined-to-form-a-polygon-in-python 
# maybe that helps a little
