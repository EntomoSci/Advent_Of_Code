'''12-13-2021, AdventCode day 5 part 1 by smv7'''

from modules import create_dots_map
from modules import find_largest_coordinate
from modules import mark_coordinates


def main():
    # Transforming the input to Python Data Structure.
    file_path = './input.txt'
    vent_lines = [] # Holds all coordinates of vent lines.
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            coor_1, coor_2 = line.split(' -> ') # Coordinates (x1,y1) and (x2,y2)
            vent_line = (tuple(coor_1.split(',')), tuple(coor_2.split(',')))
            vent_lines.append(vent_line)

    # Creating the dots map
    largest_x, largest_y = find_largest_coordinate(vent_lines)
    dots_map = create_dots_map(largest_x, largest_y)

    dots_map_marked = mark_coordinates(vent_lines, dots_map)
    print(dots_map_marked)


if __name__ == '__main__':
    main()
