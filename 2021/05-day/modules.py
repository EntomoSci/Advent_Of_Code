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


def mark_coordinates(coords_list:list, dots_map:list, diagonal:bool=None) -> list:
    '''Return a new dots map marked with the coordinates
       x1,y1 to x2,y2 from coords_list.'''

    new_dots_map = list(dots_map)
    
    for coords in coords_list:
        x1_coord = int(coords[0][0])
        y1_coord = int(coords[0][1])
        x2_coord = int(coords[1][0])
        y2_coord = int(coords[1][1])
        
        # Range of the coordinates from x1,x2 and y1,y2 sorted in ascending order.
        # Using only for horizontal and vertical vent lines.
        sorted_coords = None

        # Ranges for the diagonal vent lines.
        horizontal_range = None
        vertical_range = None

        # Create the ranges for vertical vent lines.
        if x1_coord == x2_coord:
            sorted_coords = tuple(sorted([y1_coord, y2_coord]))
            vertical_range = tuple(range(sorted_coords[0], sorted_coords[1]))

        # Create the ranges for horizontal vent lines.
        elif y1_coord == y2_coord:
            sorted_coords = tuple(sorted([x1_coord, x2_coord]))
            horizontal_range = tuple(range(sorted_coords[0], sorted_coords[1]))

        # Diagonal vent line processing.
        else:
            if diagonal:
                # Create the index range for the diagonal vent line.
                if (x1_coord < x2_coord) and (y1_coord < y2_coord): # Vent line from upper left to lower right.
                    horizontal_range = tuple(range(x1_coord, x2_coord+1))
                    vertical_range = tuple(range(y1_coord, y2_coord+1))

                elif (x1_coord > x2_coord) and (y1_coord > y2_coord): # Vent line from lower right to upper left.
                    horizontal_range = tuple(range(x2_coord, x1_coord+1))
                    vertical_range = tuple(range(y2_coord, y1_coord+1))

                elif (x1_coord > x2_coord) and (y1_coord < y2_coord): # Vent line from upper right to lower left.
                    horizontal_range = tuple(reversed(range(x2_coord, x1_coord+1)))
                    vertical_range = tuple(range(y1_coord, y2_coord+1))

                elif (x1_coord < x2_coord) and (y1_coord > y2_coord): # Vent line from lower left to upper right.
                    horizontal_range = tuple(range(x1_coord, x2_coord+1))
                    vertical_range = tuple(reversed(range(y2_coord, y1_coord+1)))

                # Mark the diagonal vent line.
                i = 0
                while i < len(horizontal_range):
                    x = horizontal_range[i]
                    y = vertical_range[i]

                    if new_dots_map[y][x] == '.':
                        new_dots_map[y][x] = 1
                    else:
                        new_dots_map[y][x] += 1
                    i += 1
                continue # Skip horizontal and vertical vent line processing.
            else:
                continue

        # Use a range of coordinates x1,x2 or y1,y2 (depending of the
        # orientation of the vent line) to mark the positions.
        # Only for horizontal and vertical vent lines.
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
