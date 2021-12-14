'''Functions to Advent Code 2021, day 5'''


def create_dots_map(x:int, y:int) -> list:
    '''Return a 2D array of "y" arrays and each array filled with "x" dots (".").'''

    dots_map = []
    # Appending the rows filled with dots to the map.
    # The function recieves coordinates (0-9) to construct the dots map and
    # because of that the "x" and "y" parameters are incremented by 1.
    i = 0
    while i < y+1:
        dots_map.append(['.' for j in range(x+1)])
        i += 1

    return dots_map


def find_largest_coordinate(sequence: list) -> tuple:
    '''Return a tuple with the largest numbers of 'x' coordinates (index 0) and 'y' (index 1)'''
    
    largest_x = 0
    largest_y = 0
    for outer in sequence:
        for inner in outer:
            x = int(inner[0])
            y = int(inner[1])
            if x > largest_x:
                largest_x = x
            if y > largest_y:
                largest_y = y

    return (largest_x, largest_y)


def mark_coordinates(coords_list:list, dots_map:list) -> list:
    '''Return a new dots map marked with the coordinates
       x1,y1 to x2,y2 from coords_list.'''

    new_dots_map = list(dots_map)
    
    for coords in coords_list:
        x1_coord = int(coords[0][0])
        y1_coord = int(coords[0][1])
        x2_coord = int(coords[1][0])
        y2_coord = int(coords[1][1])
        
        # Sort in ascending order the coordinates from x1,x2 and y1,y2.
        sorted_coords = None
        if x1_coord == x2_coord: # The vent line is vertical.
            sorted_coords = tuple(sorted([y1_coord, y2_coord]))
        elif y1_coord == y2_coord: # The vent line is horizontal.
            sorted_coords = tuple(sorted([x1_coord, x2_coord]))
        else:
            continue

        # Use a range of coordinates x1,x2 or y1,y2 (depending of the
        # orientation of the vent line) to mark the positions.
        line_range = tuple(range(sorted_coords[0], sorted_coords[1]+1)) 
        for point in line_range:
            # Vertical vent line marks.
            if x1_coord == x2_coord:
                if new_dots_map[point][x1_coord] == '.':
                    new_dots_map[point][x1_coord] = 1
                else:
                    new_dots_map[point][x1_coord] += 1        
            # Horizontal vent line marks.
            elif y1_coord == y2_coord:
                if new_dots_map[y1_coord][point] == '.':
                    new_dots_map[y1_coord][point] = 1
                else:
                    new_dots_map[y1_coord][point] += 1

    return new_dots_map
